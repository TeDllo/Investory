import telebot
from dependecies import DependencyMatcher
from users.states import BotState

TOKEN = "5459856405:AAEAdbjoytU_iWNmHDlFRO3yCocVyMnVYXw"

bot = telebot.TeleBot(TOKEN)
matcher = DependencyMatcher(bot)


def get_lambda(state: BotState):
    return lambda msg: matcher.controller.get_state(msg.from_user.id) == state


@bot.message_handler(func=get_lambda(BotState.NOT_STARTED))
def handle_not_started(message):
    matcher.handler.handle(message, BotState.NOT_STARTED)


@bot.message_handler(func=get_lambda(BotState.START))
def handle_start(message):
    matcher.handler.handle(message, BotState.START)


@bot.message_handler(func=get_lambda(BotState.TRADE_MODE))
def handle_trade_mode(message):
    matcher.handler.handle(message, BotState.TRADE_MODE)


@bot.message_handler(func=get_lambda(BotState.MY_PORTFOLIO))
def handle_my_portfolio(message):
    matcher.handler.handle(message, BotState.MY_PORTFOLIO)


@bot.message_handler(func=get_lambda(BotState.BALANCE))
def handle_balance(message):
    matcher.handler.handle(message, BotState.BALANCE)


@bot.message_handler(func=get_lambda(BotState.TRADE_START))
def handle_trade_start(message):
    matcher.handler.handle(message, BotState.TRADE_START)


bot.infinity_polling()
