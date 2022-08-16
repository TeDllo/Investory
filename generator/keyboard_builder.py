from users.states import BotState
from telebot.types import ReplyKeyboardMarkup
from resources import buttons


class KeyboardBuilder:
    def __init__(self):
        self.keyboards: dict[BotState, ReplyKeyboardMarkup] = {}

        self.create_start()
        self.create_trade_mode()
        self.create_my_portfolio()
        self.create_useful_info()
        self.create_balance()
        self.create_trade_start()
        self.create_shares_choice()

    def get_keyboard(self, state: BotState) -> ReplyKeyboardMarkup:
        return self.keyboards[state]

    def create_start(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

        keyboard.add(buttons.key_trade_mode)
        keyboard.add(buttons.key_useful, buttons.key_about)

        self.keyboards[BotState.START] = keyboard

    def create_trade_mode(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

        keyboard.add(buttons.key_start_trading, buttons.key_portfolio)
        keyboard.add(buttons.key_balance, buttons.key_quit_trade)

        self.keyboards[BotState.TRADE_MODE] = keyboard

    def create_my_portfolio(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

        keyboard.add(buttons.key_analytics, buttons.key_start_trading)
        keyboard.add(buttons.key_balance, buttons.key_quit_trade)

        self.keyboards[BotState.MY_PORTFOLIO] = keyboard

    def create_useful_info(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

        keyboard.add(buttons.key_how_to_get_portfolio)
        keyboard.add(buttons.key_checklist)

        self.keyboards[BotState.USEFUL_INFO] = keyboard

    def create_balance(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

        keyboard.add(buttons.key_portfolio, buttons.key_start_trading)

        self.keyboards[BotState.BALANCE] = keyboard

    def create_trade_start(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

        keyboard.add(buttons.key_russian_shares)
        keyboard.add(buttons.key_foreign_shares)
        keyboard.add(buttons.key_quit_game)

        self.keyboards[BotState.TRADE_START] = keyboard

    def create_shares_choice(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

        keyboard.add(buttons.key_back)

        self.keyboards[BotState.SHARES_CHOICE] = keyboard
