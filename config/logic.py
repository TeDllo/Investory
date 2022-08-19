from config.states import BotState
from telegram.handler import TransitionModule
from resources import buttons
from trade.shares.shares import ShareType, ShareController


class AppLogic:
    def __init__(self, bridge: TransitionModule, share_controller: ShareController):
        self.mapper: dict[BotState, dict[str, BotState]]
        self.bridge = bridge
        self.share_controller = share_controller

        self.any_msg = {
            BotState.SHARES_QUANTITY: BotState.SHARES_CONFIRMATION
        }

        self.mapper = {
            BotState.NOT_STARTED: {
                "/start": BotState.START
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
                buttons.key_start_trading.text: BotState.TRADE_START
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

            BotState.SHARES_SUCCESS: {
                buttons.key_continue.text: BotState.TRADE_START,
                buttons.key_quit_game.text: BotState.TRADE_MODE
            }
        }

        all_shares = self.share_controller.load_shares(ShareType.RUSSIAN)
        all_shares.extend(self.share_controller.load_shares(ShareType.FOREIGN))
        for share in all_shares:
            self.mapper[BotState.SHARES_CHOICE][share.ticker] = BotState.SHARES_INFO
