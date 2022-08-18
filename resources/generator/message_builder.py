from telebot import types

from config.messages import MessageConnector
from config.states import BotState


class MessageBuilder:
    def __init__(self, connector: MessageConnector):
        self.connector = connector

    def get_message(self, state: BotState, msg: types.Message) -> str:
        return self.connector.mapper[state].get_message(msg)
