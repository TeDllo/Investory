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
        return texts.balance.format(balance_rub, balance_usd)


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
