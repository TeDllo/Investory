import telebot
from telebot import types

from resources import buttons
from users.states import BotState
from users.controller.controller_interface import Controller
from telegram.sender import TelegramSender


class MessageHandler:
    def __init__(self,
                 bot: telebot.TeleBot,
                 controller: Controller,
                 sender: TelegramSender):
        self.bot = bot
        self.controller = controller
        self.sender = sender

    def handle_not_started(self, msg: types.Message) -> None:
        self.controller.add_user(msg.from_user.id)
        self.sender.send_start(msg)

    def handle_start(self, msg: types.Message) -> None:
        if msg.text == buttons.key_trade_mode.text:
            self.controller.set_state(msg.from_user.id, BotState.TRADE_MODE)
            self.sender.send_trade_mode(msg)
        elif msg.text == buttons.key_useful.text:
            self.sender.send_not_implemented(msg)
        elif msg.text == buttons.key_about.text:
            self.sender.send_not_implemented(msg)

    def handle_trade_mode(self, msg: types.Message) -> None:
        if msg.text == buttons.key_quit.text:
            self.controller.set_state(msg.from_user.id, BotState.START)
            self.sender.send_start(msg)
        elif msg.text == buttons.key_portfolio.text:
            self.controller.set_state(msg.from_user.id, BotState.MY_PORTFOLIO)
            self.sender.send_my_portfolio(msg)
        elif msg.text == buttons.key_balance.text:
            self.controller.set_state(msg.from_user.id, BotState.BALANCE)
            self.sender.send_balance(msg)
        elif msg.text == buttons.key_start_trading.text:
            self.sender.send_not_implemented(msg)

    def handle_my_portfolio(self, msg: types.Message) -> None:
        if msg.text == buttons.key_analytics.text:
            self.controller.set_state(msg.from_user.id, BotState.START)
            self.sender.send_analytics(msg)
        elif msg.text == buttons.key_balance.text:
            self.controller.set_state(msg.from_user.id, BotState.BALANCE)
            self.sender.send_balance(msg)
        elif msg.text == buttons.key_start_trading.text:
            self.sender.send_not_implemented(msg)
        elif msg.text == buttons.key_quit.text:
            self.controller.set_state(msg.from_user.id, BotState.START)
            self.sender.send_start(msg)

    def handle_balance(self, msg: types.Message) -> None:
        if msg.text == buttons.key_portfolio.text:
            self.controller.set_state(msg.from_user.id, BotState.MY_PORTFOLIO)
            self.sender.send_my_portfolio(msg)
        elif msg.text == buttons.key_start_trading.text:
            self.sender.send_not_implemented(msg)

    def handle_trade_start(self, msg: types.Message) -> None:
        if msg.text == buttons.key_quit.text:
            self.controller.set_state(msg.from_user.id, BotState.TRADE_MODE)
            self.sender.send_trade_mode(msg)
