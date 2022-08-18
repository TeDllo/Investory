from config.key_settings import KeySettings
from config.states import BotState
from telebot.types import ReplyKeyboardMarkup


class KeyboardBuilder:
    def __init__(self, settings: KeySettings):
        self.keyboards: dict[BotState, ReplyKeyboardMarkup] = {}
        self.settings = settings

        for state in settings.mapper:
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

            for row in settings.mapper[state]:
                keyboard.add(*row)

            self.keyboards[state] = keyboard

    def get_keyboard(self, state: BotState) -> ReplyKeyboardMarkup:
        return self.keyboards[state]
