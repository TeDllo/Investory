from telebot import types

from telegram.transition import TransitionModule
from config.states import BotState
from config.logic import AppLogic


def handle_state(state) -> BotState:
    if state is None:
        return BotState.NOT_STARTED
    return BotState(state)


def handle_message(msg: types.Message) -> types.Message:
    if len(msg.text) > 0 and msg.text[0] == '/':
        msg.text = msg.text[1:]
    return msg


class MessageHandler:
    def __init__(self, trans: TransitionModule, logic: AppLogic):
        self.trans = trans
        self.logic = logic

    def handle(self, msg: types.Message, state) -> None:
        state = handle_state(state)
        msg = handle_message(msg)
        self.handle_transition(msg, state)

    def handle_transition(self, msg: types.Message, state: BotState) -> None:
        if self.logic.has_text(state, msg.text):
            self.trans.move(msg, state, self.logic.get_next(state, msg.text))
        else:
            self.handle_any(msg, state)

    def handle_any(self, msg: types.Message, state: BotState) -> None:
        if self.logic.any(state):
            self.trans.move(msg, state, self.logic.get_next_any(state))
        else:
            self.trans.wrong_command(msg)
