import telebot
from resources import messages
from resources.keyboard_builder import KeyboardBuilder
from telebot import types
from users.states import BotState


class TelegramSender:
    def __init__(self, bot: telebot.TeleBot, keyboard_builder: KeyboardBuilder):
        self.bot = bot
        self.keyboard_builder = keyboard_builder

    def send_start(self, msg: types.Message) -> None:
        self.bot.send_message(msg.from_user.id,
                              messages.greeting,
                              reply_markup=self.keyboard_builder.get_keyboard(BotState.START))

    def send_trade_mode(self, msg: types.Message) -> None:
        self.bot.send_message(msg.from_user.id,
                              messages.trade_rules,
                              reply_markup=self.keyboard_builder.get_keyboard(BotState.TRADE_MODE))

    def send_my_portfolio(self, msg: types.Message) -> None:
        self.bot.send_message(msg.from_user.id,
                              "Список акций",
                              reply_markup=self.keyboard_builder.get_keyboard(BotState.MY_PORTFOLIO))

    def send_useful_info(self, msg: types.Message) -> None:
        self.bot.send_message(msg.from_user.id,
                              messages.useful_info,
                              reply_markup=self.keyboard_builder.get_keyboard(BotState.USEFUL_INFO))

    def send_analytics(self, msg: types.Message) -> None:
        self.bot.send_message(msg.from_user.id,
                              "Аналитика: лучше идите домой.",
                              reply_markup=self.keyboard_builder.get_keyboard(BotState.TRADE_MODE))

    def send_balance(self, msg: types.Message) -> None:
        self.bot.send_message(msg.from_user.id,
                              "Ваш баланс: 3 рубля. Идите домой.",
                              reply_markup=self.keyboard_builder.get_keyboard(BotState.BALANCE))

    def send_not_implemented(self, msg: types.Message) -> None:
        self.bot.send_message(msg.from_user.id, messages.not_implemented)
