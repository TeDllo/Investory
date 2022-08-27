from telebot import types

from telegram.transition import TransitionModule
from config.states import BotState
from config.logic import AppLogic


class MessageHandler:
    def __init__(self, trans: TransitionModule, logic: AppLogic):
        self.trans = trans
        self.logic = logic

    def handle(self, msg: types.Message, state) -> None:
        print(msg.from_user.id)

        if state is None:
            state = BotState.NOT_STARTED.value

        state = BotState(state)
        print("Current state: ", state)

        if state in self.logic.any_msg and msg.text not in self.logic.mapper[state]:
            self.trans.simple_transition(msg, state, self.logic.any_msg[state])
        else:
            options = self.logic.mapper[state]

            if msg.text not in options and state not in self.logic.any_msg:
                self.trans.wrong_command(msg)
            elif options[msg.text] == BotState.NOT_IMPLEMENTED:
                self.trans.not_implemented(msg)
            else:
                self.trans.simple_transition(msg, state, options[msg.text])
