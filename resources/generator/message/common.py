import telebot

from resources.generator.message.msg_gen import MessageGenerator
from resources import texts, buttons
from trade.shares.shares import ShareType, get_shares


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
    def get_message(self, msg: telebot.types.Message) -> str:
        share_type = ShareType.RUSSIAN \
            if msg.text == buttons.key_russian_shares.text \
            else ShareType.FOREIGN

        shares_list = "\n".join(
            map(
                lambda share: share.name + " " + share.ticker,
                get_shares(share_type)
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
