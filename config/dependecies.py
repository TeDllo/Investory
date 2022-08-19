import telebot

from config.data_handlers import DataHandlersCore
from config.key_settings import KeySettings
from config.messages import MessageConnector
from data.data_changer import DataChanger
from resources.generator.message_builder import MessageBuilder
from telegram.handler import MessageHandler
from config.logic import AppLogic
from telegram.transition import TransitionModule
from telegram.sender import TelegramSender
from resources.generator.keyboard_builder import KeyboardBuilder
from data.controller.cache_controller import CacheController
from trade.shares.shares import ShareController
from trade.trading import TradeSupplier, TradeCore

token = "t.pIrEaRy-y3G_ilahFl-fLPxSiqhKU3-nl3dv236_1Zt0jV7bksqhjtpUtwlo0B241Qa0LOdM51a-EjtJvsHZIQ"

class DependencyMatcher:
    def __init__(self, bot: telebot.TeleBot):
        self.controller = CacheController()

        self.trade_supplier = TradeSupplier(TradeCore(token))
        self.share_core = ShareController(self.trade_supplier)

        self.sender = TelegramSender(bot,
                                     self.controller,
                                     MessageBuilder(
                                         MessageConnector(
                                             self.controller,
                                             self.share_core
                                         )
                                     ),
                                     KeyboardBuilder(KeySettings()))

        self.changer = DataChanger(
            DataHandlersCore(self.controller, self.share_core),
            self.controller
        )
        self.bridge = TransitionModule(self.changer, self.sender)
        self.logic = AppLogic(self.bridge, self.share_core)

        self.handler = MessageHandler(self.bridge, self.logic)
