from config.states import BotState
from resources import buttons


class AppLogic:
    def __init__(self):
        self.mapper: dict[BotState, dict[str, BotState]]

        self.any_msg = {
            BotState.SHARES_QUANTITY: BotState.SHARES_CONFIRMATION,
            BotState.SHARES_CHOICE: BotState.SHARES_INFO,
            BotState.EXCHANGE_QUANTITY: BotState.EXCHANGE_CONFIRMATION
        }

        self.mapper = {
            BotState.NOT_STARTED: {
                "start": BotState.START
            },

            BotState.START: {
                buttons.key_trade_mode.text: BotState.TRADE_MODE,
                buttons.key_useful.text: BotState.USEFUL_INFO,
                buttons.key_about.text: BotState.ABOUT
            },

            BotState.TRADE_MODE: {
                buttons.key_quit_trade.text: BotState.START,
                buttons.key_portfolio.text: BotState.MY_PORTFOLIO,
                buttons.key_balance.text: BotState.BALANCE,
                buttons.key_start_trading.text: BotState.TRADE_START
            },

            BotState.MY_PORTFOLIO: {
                buttons.key_analytics.text: BotState.ANALYTICS,
                buttons.key_balance.text: BotState.BALANCE,
                buttons.key_start_trading.text: BotState.TRADE_START,
                buttons.key_quit_trade.text: BotState.START
            },

            BotState.BALANCE: {
                buttons.key_portfolio.text: BotState.MY_PORTFOLIO,
                buttons.key_start_trading.text: BotState.TRADE_START,
                buttons.key_quit_trade.text: BotState.START,
                buttons.key_exchange_currency.text: BotState.EXCHANGE
            },

            BotState.EXCHANGE: {
                buttons.key_buy_usd.text: BotState.EXCHANGE_QUANTITY,
                buttons.key_buy_rub.text: BotState.EXCHANGE_QUANTITY,
                buttons.key_back.text: BotState.BALANCE,
                buttons.key_quit_trade.text: BotState.START
            },

            BotState.EXCHANGE_QUANTITY: {
                buttons.key_back.text: BotState.EXCHANGE,
                buttons.key_quit_trade.text: BotState.START
            },

            BotState.EXCHANGE_CONFIRMATION: {
                buttons.key_accept.text: BotState.EXCHANGE_SUCCESS,
                buttons.key_back.text: BotState.EXCHANGE_QUANTITY,
                buttons.key_quit_trade.text: BotState.START
            },

            BotState.EXCHANGE_SUCCESS: {
                buttons.key_portfolio.text: BotState.MY_PORTFOLIO,
                buttons.key_start_trading.text: BotState.TRADE_START,
                buttons.key_quit_trade.text: BotState.START,
                buttons.key_exchange_currency.text: BotState.EXCHANGE
            },

            BotState.ANALYTICS: {
                buttons.key_quit_trade.text: BotState.START,
                buttons.key_portfolio.text: BotState.MY_PORTFOLIO,
                buttons.key_balance.text: BotState.BALANCE,
                buttons.key_start_trading.text: BotState.TRADE_START
            },

            BotState.TRADE_START: {
                buttons.key_quit_game.text: BotState.TRADE_MODE,
                buttons.key_russian_shares.text: BotState.SHARES_CHOICE,
                buttons.key_foreign_shares.text: BotState.SHARES_CHOICE
            },

            BotState.USEFUL_INFO: {
                buttons.key_how_to_get_portfolio.text: BotState.HOW_TO_MAKE_PORTFOLIO,
                buttons.key_checklist.text: BotState.CHECK_LIST,
                buttons.key_back.text: BotState.START
            },

            BotState.HOW_TO_MAKE_PORTFOLIO: {
                buttons.key_trade_mode.text: BotState.TRADE_MODE,
                buttons.key_about.text: BotState.ABOUT,
                buttons.key_checklist.text: BotState.CHECK_LIST
            },

            BotState.CHECK_LIST: {
                buttons.key_trade_mode.text: BotState.TRADE_MODE,
                buttons.key_about.text: BotState.ABOUT,
                buttons.key_how_to_get_portfolio.text: BotState.HOW_TO_MAKE_PORTFOLIO
            },

            BotState.ABOUT: {
                buttons.key_useful.text: BotState.USEFUL_INFO,
                buttons.key_trade_mode.text: BotState.TRADE_MODE
            },

            BotState.SHARES_CHOICE: {
                buttons.key_back.text: BotState.TRADE_START
            },

            BotState.SHARES_INFO: {
                buttons.key_buy.text: BotState.SHARES_QUANTITY,
                buttons.key_sell.text: BotState.SHARES_QUANTITY,
                buttons.key_back.text: BotState.TRADE_START,
                buttons.key_quit_game.text: BotState.TRADE_MODE
            },

            BotState.SHARES_QUANTITY: {
                buttons.key_back.text: BotState.SHARES_INFO
            },

            BotState.SHARES_CONFIRMATION: {
                buttons.key_accept.text: BotState.SHARES_SUCCESS,
                buttons.key_back.text: BotState.SHARES_QUANTITY,
                buttons.key_quit_game.text: BotState.TRADE_MODE
            },

            BotState.SHARES_CURRENCY_OFFER: {
                buttons.key_exchange_trade_accept.text: BotState.SHARES_SUCCESS,
                buttons.key_back.text: BotState.SHARES_QUANTITY,
                buttons.key_quit_game.text: BotState.TRADE_MODE
            },

            BotState.SHARES_SUCCESS: {
                buttons.key_continue.text: BotState.TRADE_START,
                buttons.key_quit_game.text: BotState.TRADE_MODE
            }
        }

    def any(self, state: BotState) -> bool:
        return state in self.any_msg

    def has_text(self, state: BotState, text: str) -> bool:
        return text in self.mapper[state]

    def get_next(self, state: BotState, text: str) -> BotState:
        return self.mapper[state][text]

    def get_next_any(self, state: BotState) -> BotState:
        return self.any_msg[state]
