from users.states import BotState
from typing import Callable
from telegram.handler import TransitionModule
from resources import buttons, messages


class AppLogic:
    def __init__(self, bridge: TransitionModule):
        self.mapper: dict[BotState, dict[str, Callable]]
        self.bridge = bridge

        self.mapper = {
            BotState.NOT_STARTED: {
                "/start": self.bridge.to_start
            },

            BotState.START: {
                buttons.key_trade_mode.text: self.bridge.to_trade_mode,
                buttons.key_useful.text: self.bridge.NOT_IMPLEMENTED,
                buttons.key_about.text: self.bridge.NOT_IMPLEMENTED
            },

            BotState.TRADE_MODE: {
                buttons.key_quit_trade.text: self.bridge.to_start,
                buttons.key_portfolio.text: self.bridge.to_my_portfolio,
                buttons.key_balance.text: self.bridge.to_balance,
                buttons.key_start_trading.text: self.bridge.to_trade_start
            },

            BotState.MY_PORTFOLIO: {
                buttons.key_analytics.text: self.bridge.to_analytics,
                buttons.key_balance.text: self.bridge.to_balance,
                buttons.key_start_trading.text: self.bridge.to_trade_start,
                buttons.key_quit_trade.text: self.bridge.to_start
            },

            BotState.BALANCE: {
                buttons.key_portfolio.text: self.bridge.to_my_portfolio,
                buttons.key_start_trading.text: self.bridge.to_trade_start
            },

            BotState.TRADE_START: {
                buttons.key_quit_trade.text: self.bridge.to_trade_mode,
                buttons.key_russian_shares.text: self.bridge.to_shares_choice,
                buttons.key_foreign_shares.text: self.bridge.to_shares_choice
            }
        }

        for state in self.mapper:
            self.mapper[state][messages.incorrect_flag] = self.bridge.wrong_command
