import telebot
from generator.keyboard_builder import KeyboardBuilder
from telebot import types

from resources import messages
from users.states import BotState
from users.controller.controller_interface import Controller
from generator.message_builder import MessageBuilder


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

    def send_start(self, msg: types.Message) -> None:
        self.bot.send_message(msg.from_user.id,
                              self.message_builder.get_message(BotState.START),
                              reply_markup=self.keyboard_builder.get_keyboard(BotState.START))

    def send_trade_mode(self, msg: types.Message) -> None:
        self.bot.send_message(msg.from_user.id,
                              self.message_builder.get_message(BotState.TRADE_MODE),
                              reply_markup=self.keyboard_builder.get_keyboard(BotState.TRADE_MODE))

    def send_my_portfolio(self, msg: types.Message) -> None:
        self.bot.send_message(msg.from_user.id,
                              self.message_builder.get_message(BotState.MY_PORTFOLIO, msg.from_user.id),
                              reply_markup=self.keyboard_builder.get_keyboard(BotState.MY_PORTFOLIO))

    def send_useful_info(self, msg: types.Message) -> None:
        self.bot.send_message(msg.from_user.id,
                              self.message_builder.get_message(BotState.USEFUL_INFO),
                              reply_markup=self.keyboard_builder.get_keyboard(BotState.USEFUL_INFO))

    def send_analytics(self, msg: types.Message) -> None:
        self.bot.send_message(msg.from_user.id,
                              self.message_builder.get_message(BotState.ANALYTICS),
                              reply_markup=self.keyboard_builder.get_keyboard(BotState.TRADE_MODE))

    def send_balance(self, msg: types.Message) -> None:
        self.bot.send_message(msg.from_user.id, self.message_builder.get_message(BotState.BALANCE, msg.from_user.id),
                              reply_markup=self.keyboard_builder.get_keyboard(BotState.BALANCE))

    def send_not_implemented(self, msg: types.Message) -> None:
        self.bot.send_message(msg.from_user.id, messages.not_implemented)
