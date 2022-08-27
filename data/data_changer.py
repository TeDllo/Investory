import telebot
import telebot.types as tt

from config.data_handlers import DataHandlersCore
from config.states import BotState
from data.controller.controller_interface import Controller


class DataChanger:
    def __init__(self,
                 data_handler: DataHandlersCore,
                 bot: telebot.TeleBot,
                 controller: Controller
                 ):
        self.data_handler = data_handler
        self.bot = bot
        self.controller = controller

    def proceed(self,
                msg: tt.Message,
                state_from: BotState,
                state_to: BotState):
        if state_from == BotState.NOT_STARTED and not self.controller.has_user(msg.from_user.id):
            self.controller.add_user(msg.from_user.id)

        if state_from in self.data_handler.mapper:
            self.data_handler.mapper[state_from].handle(msg)

        self.bot.set_state(msg.from_user.id, state_to.value)
