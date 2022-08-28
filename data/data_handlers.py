from telebot import types
from tinvest import Currency

from data.controller.controller_interface import Controller
from data.types import Action, Transaction
from resources import buttons, texts
from trade.shares.shares import ShareController


class DataError(Exception):
    def __init__(self, message):
        self.message = message


class NotEnoughCurrencyError(Exception):
    pass


class DataHandler:
    def handle(self, msg: types.Message) -> None:
        pass

    def check(self, msg: types.Message) -> None:
        pass


class SharesChoiceHandler(DataHandler):
    def __init__(self, controller: Controller, share_core: ShareController):
        self.controller = controller
        self.share_core = share_core

    def handle(self, msg: types.Message) -> None:
        self.check(msg)
        if msg.text != buttons.key_back.text:
            self.controller.set_share(msg.from_user.id,
                                      self.share_core.get_share(msg.text))
            self.controller.set_price(msg.from_user.id,
                                      self.share_core.get_price(msg.text))

    def check(self, msg: types.Message) -> None:
        if msg.text != buttons.key_back.text and not self.share_core.exists(msg.text):
            raise DataError("Вы ввели неправильный тикер.")


class SharesInfoHandler(DataHandler):
    def __init__(self, controller: Controller):
        self.controller = controller

    def handle(self, msg: types.Message) -> None:
        if msg.text == buttons.key_buy.text:
            self.controller.set_action(msg.from_user.id, Action.BUY)
        elif msg.text == buttons.key_sell.text:
            self.controller.set_action(msg.from_user.id, Action.SELL)


class SharesQuantityHandler(DataHandler):
    def __init__(self, controller: Controller):
        self.controller = controller

    def handle(self, msg: types.Message) -> None:
        if msg.text != buttons.key_back.text:
            self.check(msg)
            self.controller.set_quantity(msg.from_user.id, int(msg.text))

    def check(self, msg: types.Message) -> None:
        if not msg.text.isnumeric() or int(msg.text) <= 0:
            raise DataError("Введите ЦЕЛОЕ ПОЛОЖИТЕЛЬНОЕ число, епт")


class SharesConfirmationHandler(DataHandler):
    def __init__(self, controller: Controller, share_core: ShareController):
        self.controller = controller
        self.share_core = share_core

    def handle(self, msg: types.Message) -> None:
        if msg.text != buttons.key_accept.text:
            return

        operation = self.controller.get_operation(msg.from_user.id)
        if operation.action == Action.BUY:
            self.handle_buy(msg, operation)
        elif operation.action == Action.SELL:
            self.handle_sell(msg, operation)
        else:
            raise DataError("Ошибка: действие не назначено.")

        self.controller.accept_trade(msg.from_user.id)

    def handle_buy(self, msg: types.Message, operation: Transaction) -> None:
        delta: float = operation.total - self.controller.get_balance(msg.from_user.id, operation.share.currency)

        if delta <= 0:
            return

        exchange_rate = self.share_core.get_currency_price(Currency.usd)

        if operation.share.currency == Currency.usd:
            total_need = delta * exchange_rate
            currency_have = Currency.rub
        else:
            total_need = delta / exchange_rate
            currency_have = Currency.usd

        enough_another = self.controller.get_balance(msg.from_user.id, currency_have) >= total_need

        if enough_another:
            self.controller.set_currency(msg.from_user.id, operation.share.currency)
            self.controller.set_currency_price(msg.from_user.id, exchange_rate)
            self.controller.set_currency_quantity(msg.from_user.id, delta)

            raise NotEnoughCurrencyError()
        raise DataError("Недостаточно денег на балансе")

    def handle_sell(self, msg: types.Message, operation: Transaction) -> None:
        portfolio = self.controller.get_portfolio(msg.from_user.id)
        position = list(filter(lambda obj: obj.share.ticker == operation.share.ticker, portfolio))
        if len(position) == 0:
            raise DataError("В Вашем портфеле нет данной акции.")

        position = position[0]

        if operation.quantity > position.quantity:
            raise DataError(
                texts.shares_not_enough.format(
                    operation.quantity,
                    position.quantity
                )
            )


class SharesCurrencyOffer(DataHandler):
    def __init__(self, controller: Controller):
        self.controller = controller

    def handle(self, msg: types.Message) -> None:
        if msg.text == buttons.key_exchange_trade_accept.text:
            self.controller.accept_exchange(msg.from_user.id)
            self.controller.accept_trade(msg.from_user.id)

    def check(self, msg: types.Message) -> None:
        pass


class BalanceHandler(DataHandler):
    def __init__(self, controller: Controller, share_core: ShareController):
        self.controller = controller
        self.share_core = share_core

    def handle(self, msg: types.Message) -> None:
        if msg.text == buttons.key_exchange_currency.text:
            self.controller.set_currency_price(msg.from_user.id,
                                               self.share_core.get_currency_price(Currency.usd))

    def check(self, msg: types.Message) -> None:
        pass


class ExchangeHandler(DataHandler):
    def __init__(self, controller: Controller):
        self.controller = controller

    def handle(self, msg: types.Message) -> None:
        if msg.text == buttons.key_buy_rub.text:
            self.controller.set_currency(msg.from_user.id, Currency.rub)
        elif msg.text == buttons.key_buy_usd.text:
            self.controller.set_currency(msg.from_user.id, Currency.usd)

    def check(self, msg: types.Message) -> None:
        pass


class ExchangeQuantityHandler(DataHandler):
    def __init__(self, controller: Controller):
        self.controller = controller

    def handle(self, msg: types.Message) -> None:
        if msg.text not in [buttons.key_back.text, buttons.key_quit_trade.text]:
            self.check(msg)
            self.controller.set_currency_quantity(msg.from_user.id, float(msg.text))

    def check(self, msg: types.Message) -> None:
        if not msg.text.isnumeric() or float(msg.text) <= 0:
            raise DataError("Введите ПОЛОЖИТЕЛЬНОЕ число, епт")


class ExchangeConfirmationHandler(DataHandler):
    def __init__(self, controller: Controller):
        self.controller = controller

    def handle(self, msg: types.Message) -> None:
        if msg.text != buttons.key_accept.text:
            return

        currency = self.controller.get_currency(msg.from_user.id)
        quantity = self.controller.get_currency_quantity(msg.from_user.id)
        price = self.controller.get_currency_price(msg.from_user.id)

        balance_from = self.controller.get_balance(msg.from_user.id, Currency.usd)
        balance_to = self.controller.get_balance(msg.from_user.id, Currency.rub)

        total = round(quantity / price, 2)

        if currency == Currency.usd:
            balance_from, balance_to = balance_to, balance_from
            total = round(quantity * price, 2)

        if balance_from < total:
            raise DataError("Недостаточно валюты на балансе")

        self.controller.accept_exchange(msg.from_user.id)
