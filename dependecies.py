import telebot

from generator.message_builder import MessageBuilder
from telegram.handler import MessageHandler
from telegram.logic import AppLogic
from telegram.transition import TransitionModule
from telegram.sender import TelegramSender
from generator.keyboard_builder import KeyboardBuilder
from users.controller.cache_controller import CacheController


class DependencyMatcher:
    def __init__(self, bot: telebot.TeleBot):
        self.controller = CacheController()

        self.sender = TelegramSender(bot,
                                     self.controller,
                                     MessageBuilder(self.controller),
                                     KeyboardBuilder())

        self.bridge = TransitionModule(self.controller, self.sender)
        self.logic = AppLogic(self.bridge)

        self.handler = MessageHandler(self.bridge, self.logic)
