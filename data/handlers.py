from telebot import types

from data.controller.controller_interface import Controller
from data.transaction import Transaction
from resources import buttons, texts
from trade.shares.shares import ShareController, Action


class IncorrectDataError(Exception):
    def __init__(self, message):
        self.message = message


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
        if msg.text != buttons.key_back.text and self.share_core.get_share(msg.text) is None:
            raise IncorrectDataError("Вы ввели неправильный тикер.")


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
        if not msg.text.isnumeric() or int(msg.text) < 0:
            raise IncorrectDataError("Введите ЦЕЛОЕ НЕОТРИЦАТЕЛЬНОЕ число, епт")


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
            raise IncorrectDataError("Ошибка: действие не назначено.")

        self.controller.accept_trade(msg.from_user.id)

    def handle_buy(self, msg: types.Message, operation: Transaction) -> None:
        if operation.price > self.controller.get_balance(msg.from_user.id):
            raise IncorrectDataError("Недостаточно денег на балансе.")

    def handle_sell(self, msg: types.Message, operation: Transaction) -> None:
        portfolio = self.controller.get_portfolio(msg.from_user.id)
        if operation.share not in portfolio:
            raise IncorrectDataError("В Вашем портфеле нет данной акции.")

        if operation.quantity > portfolio[operation.share]:
            raise IncorrectDataError(
                texts.shares_not_enough.format(
                    operation.quantity,
                    portfolio[operation.share]
                )
            )
