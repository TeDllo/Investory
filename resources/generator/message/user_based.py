import telebot

from resources import texts
from resources.generator.message.msg_gen import MessageGenerator
from data.controller.controller_interface import Controller


class AnalyticsGenerator(MessageGenerator):
    def get_message(self, msg: telebot.types.Message) -> str:
        return "Аналитика: лучше идите домой"


class BalanceGenerator(MessageGenerator):
    def __init__(self, controller: Controller):
        self.controller = controller

    def get_message(self, msg: telebot.types.Message) -> str:
        balance = self.controller.get_balance(msg.from_user.id)
        return texts.balance.format(balance)


class MyPortfolioGenerator(MessageGenerator):
    def __init__(self, controller: Controller):
        self.controller = controller

    def get_message(self, msg: telebot.types.Message) -> str:
        return texts.my_portfolio + self.controller.get_portfolio_text(msg.from_user.id)


class SharesConfirmationGenerator(MessageGenerator):
    def __init__(self, controller: Controller):
        self.controller = controller

    def get_message(self, msg: telebot.types.Message) -> str:
        op = self.controller.get_operation(msg.from_user.id)
        return texts.shares_confirmation.format(op.action.value, op.share.name, op.quantity)


class SharesSuccessGenerator(MessageGenerator):
    def __init__(self, controller: Controller):
        self.controller = controller

    def get_message(self, msg: telebot.types.Message) -> str:
        return texts.shares_success + self.controller.get_portfolio_text(msg.from_user.id)
