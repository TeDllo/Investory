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


class DependencyMatcher:
    def __init__(self, bot: telebot.TeleBot):
        self.controller = CacheController()
        self.share_core = ShareController()

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
        self.logic = AppLogic(self.bridge)

        self.handler = MessageHandler(self.bridge, self.logic)
