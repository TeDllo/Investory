from config.states import BotState
from telebot.types import KeyboardButton
from resources import buttons


class KeySettings:
    def __init__(self):
        self.mapper: dict[BotState, list[list[KeyboardButton]]] = {
            BotState.START: [
                [buttons.key_trade_mode],
                [buttons.key_useful, buttons.key_about]
            ],

            BotState.TRADE_MODE: [
                [buttons.key_start_trading, buttons.key_portfolio],
                [buttons.key_balance, buttons.key_quit_trade]
            ],

            BotState.MY_PORTFOLIO: [
                [buttons.key_analytics, buttons.key_start_trading],
                [buttons.key_balance, buttons.key_quit_trade]
            ],

            BotState.ANALYTICS: [
                [buttons.key_start_trading, buttons.key_portfolio],
                [buttons.key_balance, buttons.key_quit_trade]
            ],

            BotState.USEFUL_INFO: [
                [buttons.key_how_to_get_portfolio],
                [buttons.key_checklist],
                [buttons.key_back]
            ],

            BotState.HOW_TO_MAKE_PORTFOLIO: [
                [buttons.key_trade_mode],
                [buttons.key_about, buttons.key_checklist]
            ],

            BotState.CHECK_LIST: [
                [buttons.key_trade_mode],
                [buttons.key_about, buttons.key_how_to_get_portfolio]
            ],

            BotState.ABOUT: [
                [buttons.key_useful],
                [buttons.key_trade_mode]
            ],

            BotState.BALANCE: [
                [buttons.key_portfolio, buttons.key_start_trading]
            ],

            BotState.TRADE_START: [
                [buttons.key_russian_shares],
                [buttons.key_foreign_shares],
                [buttons.key_quit_game]
            ],

            BotState.SHARES_CHOICE: [
                [buttons.key_back]
            ],


            BotState.SHARES_INFO: [
                [buttons.key_buy, buttons.key_sell],
                [buttons.key_back, buttons.key_quit_game]
            ],

            BotState.SHARES_QUANTITY: [
                [buttons.key_back]
            ],

            BotState.SHARES_CONFIRMATION: [
                [buttons.key_accept],
                [buttons.key_back, buttons.key_quit_game]
            ],

            BotState.SHARES_SUCCESS: [
                [buttons.key_continue],
                [buttons.key_quit_game]
            ]
        }
