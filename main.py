import telebot
from telegram.handler import MessageHandler
from telegram.sender import TelegramSender
from resources.keyboard_builder import KeyboardBuilder
from users.controller.cache_controller import CacheController

from users.states import BotState

TOKEN = "5459856405:AAEAdbjoytU_iWNmHDlFRO3yCocVyMnVYXw"

bot = telebot.TeleBot(TOKEN)

controller = CacheController()
sender = TelegramSender(bot, KeyboardBuilder())

handler = MessageHandler(bot, controller, sender)


def get_lambda(state: BotState):
    return lambda msg: controller.get_state(msg.from_user.id) == state


@bot.message_handler(func=get_lambda(BotState.NOT_STARTED))
def handle_not_started(message):
    handler.handle_not_started(message)


@bot.message_handler(func=get_lambda(BotState.START))
def handle_start(message):
    handler.handle_start(message)


@bot.message_handler(func=get_lambda(BotState.TRADE_MODE))
def handle_trade_mode(message):
    handler.handle_trade_mode(message)


@bot.message_handler(func=get_lambda(BotState.MY_PORTFOLIO))
def handle_my_portfolio(message):
    handler.handle_my_portfolio(message)


@bot.message_handler(func=get_lambda(BotState.BALANCE))
def handle_balance(message):
    handler.handle_balance(message)


bot.infinity_polling()
