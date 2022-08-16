from telebot import types

from telegram.transition import TransitionModule
from users.states import BotState
from telegram.logic import AppLogic
from resources.messages import incorrect_flag


class MessageHandler:
    def __init__(self, trans: TransitionModule, logic: AppLogic):
        self.trans = trans
        self.logic = logic

    def handle(self, msg: types.Message, state: BotState) -> None:
        options = self.logic.mapper[state]

        if msg.text not in options:
            msg.text = incorrect_flag

        options[msg.text](msg)

    # def handle_not_started(self, msg: types.Message) -> None:
    #     self.trans.to_start(msg)

    # def handle_start(self, msg: types.Message) -> None:
    #     if msg.text == buttons.key_trade_mode.text:
    #         self.trans.to_trade_mode(msg)
    #     elif msg.text == buttons.key_useful.text:
    #         self.trans.NOT_IMPLEMENTED(msg)
    #     elif msg.text == buttons.key_about.text:
    #         self.trans.NOT_IMPLEMENTED(msg)

    # def handle_trade_mode(self, msg: types.Message) -> None:
    #     if msg.text == buttons.key_quit_trade.text:
    #         self.trans.to_start(msg)
    #     elif msg.text == buttons.key_portfolio.text:
    #         self.trans.to_my_portfolio(msg)
    #     elif msg.text == buttons.key_balance.text:
    #         self.trans.to_balance(msg)
    #     elif msg.text == buttons.key_start_trading.text:
    #         self.trans.to_trade_start(msg)

    # def handle_my_portfolio(self, msg: types.Message) -> None:
    #     if msg.text == buttons.key_analytics.text:
    #         self.trans.to_analytics(msg)
    #     elif msg.text == buttons.key_balance.text:
    #         self.trans.to_balance(msg)
    #     elif msg.text == buttons.key_start_trading.text:
    #         self.trans.to_trade_start(msg)
    #     elif msg.text == buttons.key_quit_trade.text:
    #         self.trans.to_start(msg)

    # def handle_balance(self, msg: types.Message) -> None:
    #     if msg.text == buttons.key_portfolio.text:
    #         self.trans.to_my_portfolio(msg)
    #     elif msg.text == buttons.key_start_trading.text:
    #         self.trans.to_trade_start(msg)

    # def handle_trade_start(self, msg: types.Message) -> None:
    #     if msg.text == buttons.key_quit_trade.text:
    #         self.trans.to_trade_mode(msg)
    #     elif msg.text in [buttons.key_russian_shares.text, buttons.key_foreign_shares.text]:
    #         self.trans.to_shares_choice(msg)
