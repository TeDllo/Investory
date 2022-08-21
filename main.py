import telebot

from config.dependecies import DependencyMatcher

TOKEN = "5459856405:AAEAdbjoytU_iWNmHDlFRO3yCocVyMnVYXw"

bot = telebot.TeleBot(TOKEN)
matcher = DependencyMatcher(bot)


@bot.message_handler(func=lambda msg: True)
def handle_message(message):
    state = matcher.controller.get_state(message.from_user.id)
    matcher.handler.handle(message, state)


bot.infinity_polling()
