import telebot
from resources.generator.keyboard_builder import KeyboardBuilder
from telebot import types

from resources import texts
from config.states import BotState
from data.controller.controller_interface import Controller
from resources.generator.message_builder import MessageBuilder


class TelegramSender:
    def __init__(self,
                 bot: telebot.TeleBot,
                 controller: Controller,
                 message_builder: MessageBuilder,
                 keyboard_builder: KeyboardBuilder):
        self.bot = bot
        self.controller = controller
        self.message_builder = message_builder
        self.keyboard_builder = keyboard_builder

    def send_error(self, msg: types.Message, error_text: str) -> None:
        self.bot.send_message(msg.from_user.id, error_text)

    def send_wrong_command(self, msg: types.Message) -> None:
        self.bot.send_message(msg.from_user.id, texts.wrong_command)

    def send_not_implemented(self, msg: types.Message) -> None:
        self.bot.send_message(msg.from_user.id, texts.not_implemented)

    def send(self, msg: types.Message, state: BotState):
        self.bot.send_message(msg.from_user.id,
                              self.message_builder.get_message(state, msg),
                              reply_markup=self.keyboard_builder.get_keyboard(state))
