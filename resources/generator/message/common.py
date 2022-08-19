import telebot

from resources.generator.message.msg_gen import MessageGenerator
from resources import texts, buttons
from trade.shares.shares import ShareType, ShareController


class AboutGenerator(MessageGenerator):
    def get_message(self, msg: telebot.types.Message) -> str:
        return texts.about


class CheckListGenerator(MessageGenerator):
    def get_message(self, msg: telebot.types.Message) -> str:
        return texts.check_list


class HowToMakePortfolioGenerator(MessageGenerator):
    def get_message(self, msg: telebot.types.Message) -> str:
        return texts.how_to_make_portfolio


class SharesChoiceGenerator(MessageGenerator):
    def __init__(self, share_controller: ShareController):
        self.share_controller = share_controller

    def get_message(self, msg: telebot.types.Message) -> str:
        if msg.text == buttons.key_russian_shares.text:
            share_type = ShareType.RUSSIAN
        else:
            share_type = ShareType.FOREIGN

        shares_list = "\n".join(
            map(
                lambda share: share.name + " " + share.ticker,
                self.share_controller.load_shares(share_type)
            )
        )
        return texts.shares_list + shares_list


class SharesQuantityGenerator(MessageGenerator):
    def get_message(self, msg: telebot.types.Message) -> str:
        return texts.shares_quantity


class StartGenerator(MessageGenerator):
    def get_message(self, msg: telebot.types.Message) -> str:
        return texts.greeting


class TradeModeGenerator(MessageGenerator):
    def get_message(self, msg: telebot.types.Message) -> str:
        return texts.trade_rules


class TradeStartGenerator(MessageGenerator):
    def get_message(self, msg: telebot.types.Message) -> str:
        return texts.trade_start


class UsefulGenerator(MessageGenerator):
    def get_message(self, msg: telebot.types.Message) -> str:
        return texts.useful_info
