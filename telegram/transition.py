from resources import buttons
from resources.shares import ShareType
from users.controller.controller_interface import Controller
from telegram.sender import TelegramSender
from users.states import BotState


class TransitionModule:
    def __init__(self,
                 controller: Controller,
                 sender: TelegramSender
                 ):
        self.controller = controller
        self.sender = sender

    def wrong_command(self, msg):
        self.sender.send_wrong_command(msg)

    def NOT_IMPLEMENTED(self, msg):
        self.sender.send_not_implemented(msg)

    def to_start(self, msg):
        self.controller.set_state(msg.from_user.id, BotState.START)
        self.sender.send_start(msg)

    def to_trade_mode(self, msg):
        self.controller.set_state(msg.from_user.id, BotState.TRADE_MODE)
        self.sender.send_trade_mode(msg)

    def to_my_portfolio(self, msg):
        self.controller.set_state(msg.from_user.id, BotState.MY_PORTFOLIO)
        self.sender.send_my_portfolio(msg)

    def to_balance(self, msg):
        self.controller.set_state(msg.from_user.id, BotState.BALANCE)
        self.sender.send_balance(msg)

    def to_analytics(self, msg):
        self.controller.set_state(msg.from_user.id, BotState.TRADE_MODE)
        self.sender.send_analytics(msg)

    def to_trade_start(self, msg):
        self.controller.set_state(msg.from_user.id, BotState.TRADE_START)
        self.sender.send_trade_start(msg)

    def to_shares_choice(self, msg):
        share_type = ShareType.RUSSIAN \
            if msg.text == buttons.key_russian_shares.text \
            else ShareType.FOREIGN

        self.controller.set_state(msg.from_user.id, BotState.SHARES_CHOICE)
        self.sender.send_shares_choice(msg, share_type)
