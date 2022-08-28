import telebot
from tinvest import Currency

from data.controller.controller_interface import Controller
from resources import texts
from resources.generator.message.msg_gen import MessageGenerator
from trade.shares.shares import ShareController


class SharesInfoGenerator(MessageGenerator):
    def __init__(self,
                 controller: Controller,
                 share_core: ShareController):
        self.controller = controller
        self.share_core = share_core

        self.signs = {
            Currency.rub: "₽",
            Currency.usd: "$"
        }

    def get_message(self, msg: telebot.types.Message) -> str:
        share = self.controller.get_share(msg.from_user.id)
        return texts.shares_info.format(
            share.name,
            self.controller.get_price(msg.from_user.id),
            self.signs[share.currency],
            share.lot_size
        )


class ExchangeGenerator(MessageGenerator):
    def __init__(self, share_core: ShareController):
        self.share_core = share_core

    def get_message(self, msg: telebot.types.Message) -> str:
        return texts.exchange_rate.format(self.share_core.get_currency_price(Currency.usd))
