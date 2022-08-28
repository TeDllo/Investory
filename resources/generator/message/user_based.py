import telebot
from tinvest import Currency

from data.controller.controller_interface import Controller
from data.types import Position
from resources import texts
from resources.generator.message.msg_gen import MessageGenerator


def portfolio_to_text(portfolio: list[Position]) -> str:
    text = ""

    for position in portfolio:
        text += texts.portfolio_share.format(position.share.name, position.quantity)

    if len(text) == 0:
        text = texts.portfolio_empty

    return text


class AnalyticsGenerator(MessageGenerator):
    def get_message(self, msg: telebot.types.Message) -> str:
        return "Аналитика: лучше идите домой"


class BalanceGenerator(MessageGenerator):
    def __init__(self, controller: Controller):
        self.controller = controller

    def get_message(self, msg: telebot.types.Message) -> str:
        balance_rub = self.controller.get_balance(msg.from_user.id, Currency.rub)
        balance_usd = self.controller.get_balance(msg.from_user.id, Currency.usd)
        return texts.balance.format(round(balance_rub, 2), round(balance_usd, 2))


class MyPortfolioGenerator(MessageGenerator):
    def __init__(self, controller: Controller):
        self.controller = controller

    def get_message(self, msg: telebot.types.Message) -> str:
        portfolio = self.controller.get_portfolio(msg.from_user.id)

        return texts.my_portfolio + portfolio_to_text(portfolio)


class SharesConfirmationGenerator(MessageGenerator):
    def __init__(self, controller: Controller):
        self.controller = controller

        self.signs = {
            Currency.rub: "₽",
            Currency.usd: "$"
        }

    def get_message(self, msg: telebot.types.Message) -> str:
        op = self.controller.get_operation(msg.from_user.id)
        return texts.shares_confirmation.format(
            op.action.value,
            op.share.name,
            op.quantity,
            round(op.total, 2),
            self.signs[op.share.currency]
        )


class SharesSuccessGenerator(MessageGenerator):
    def __init__(self, controller: Controller):
        self.controller = controller

    def get_message(self, msg: telebot.types.Message) -> str:
        portfolio = self.controller.get_portfolio(msg.from_user.id)
        return texts.shares_success + portfolio_to_text(portfolio)


class ExchangeQuantityGenerator(MessageGenerator):
    def __init__(self, controller: Controller):
        self.controller = controller

    def get_message(self, msg: telebot.types.Message) -> str:
        currency = self.controller.get_currency(msg.from_user.id)

        sign = '₽'
        if currency == Currency.usd:
            sign = '$'

        return texts.exchange_offer.format(sign)


class ExchangeConfirmationGenerator(MessageGenerator):
    def __init__(self, controller: Controller):
        self.controller = controller

    def get_message(self, msg: telebot.types.Message) -> str:
        quantity = self.controller.get_currency_quantity(msg.from_user.id)
        price = self.controller.get_currency_price(msg.from_user.id)
        total = round(quantity / price, 2)

        currency = self.controller.get_currency(msg.from_user.id)

        sign1 = '₽'
        sign2 = '$'
        if currency == Currency.usd:
            sign1, sign2 = sign2, sign1
            total = round(price * quantity, 2)

        return texts.exchange_confirmation.format(quantity, sign1, total, sign2)


class ExchangeSuccessGenerator(MessageGenerator):
    def __init__(self, balance_generator: BalanceGenerator):
        self.balance_generator = balance_generator

    def get_message(self, msg: telebot.types.Message) -> str:
        return texts.exchange_success + self.balance_generator.get_message(msg)


class SharesCurrencyOfferGenerator(MessageGenerator):
    def __init__(self, controller: Controller):
        self.controller = controller

        self.signs = {
            Currency.rub: "₽",
            Currency.usd: "$"
        }

    def get_message(self, msg: telebot.types.Message) -> str:
        exchange_rate = self.controller.get_currency_price(msg.from_user.id)

        currency_need = self.controller.get_currency(msg.from_user.id)
        currency_have = Currency.rub if currency_need == Currency.usd else Currency.usd

        quantity = self.controller.get_currency_quantity(msg.from_user.id)

        if currency_need == Currency.usd:
            total = round(quantity * exchange_rate, 2)
        else:
            total = round(quantity / exchange_rate, 2)

        return texts.shares_currency_offer.format(
            total,
            self.signs[currency_have],
            quantity,
            self.signs[currency_need],
            exchange_rate
        )
