from config.states import BotState
from data.data_changer import DataChanger
from data.handlers import DataError, NotEnoughCurrencyError
from telegram.sender import TelegramSender


class TransitionModule:
    def __init__(self,
                 changer: DataChanger,
                 sender: TelegramSender
                 ):
        self.changer = changer
        self.sender = sender

    def wrong_command(self, msg):
        self.sender.send_wrong_command(msg)

    def move(self, msg, state_from: BotState, state_to: BotState):
        print("From {} to {}".format(state_from.name, state_to.name))

        try:
            self.changer.proceed(msg, state_from, state_to)
            self.sender.send(msg, state_to)
        except DataError as error:
            self.sender.send_error(msg, error.message)
        except NotEnoughCurrencyError:
            self.sender.send(msg, BotState.SHARES_CURRENCY_OFFER)
