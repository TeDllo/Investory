from users.states import BotState
from users.controller.controller_interface import Controller
from resources import messages
from resources.shares import ShareType, get_shares


class MessageGenerator:
    def __init__(self, controller: Controller):
        self.controller = controller

    def generate_message(self,
                         state: BotState,
                         id: int,
                         share_type: ShareType) -> str:
        if state == BotState.START:
            return self.generate_start()
        elif state == BotState.TRADE_MODE:
            return self.generate_trade_rules()
        elif state == BotState.MY_PORTFOLIO:
            return self.generate_my_portfolio(id)
        elif state == BotState.USEFUL_INFO:
            return self.generate_useful_info()
        elif state == BotState.ANALYTICS:
            return self.generate_analytics(id)
        elif state == BotState.BALANCE:
            return self.generate_balance(id)
        elif state == BotState.SHARES_CHOICE:
            return self.generate_shares(share_type)
        elif state == BotState.TRADE_START:
            return self.generate_trade_start()
        elif state == BotState.SHARES_CHOICE:
            return self.generate_shares(share_type)

    def generate_start(self):
        return messages.greeting

    def generate_trade_rules(self):
        return messages.trade_rules

    def generate_my_portfolio(self, id: int):
        return "Список акций:"

    def generate_useful_info(self):
        return messages.useful_info

    def generate_analytics(self, id: int):
        return "Аналитика: лучше идите домой."

    def generate_balance(self, id: int):
        balance = self.controller.get_balance(id)
        return f'Ваш баланс: {balance} ₽.'

    def generate_trade_start(self):
        return messages.trade_start

    def generate_shares(self, share_type: ShareType):
        return messages.shares_list + "\n".join(get_shares(share_type))


class MessageBuilder:
    def __init__(self, controller: Controller):
        self.generator = MessageGenerator(controller)

    def get_message(self, state: BotState, id=0, share_type=None) -> str:
        return self.generator.generate_message(state, id, share_type)
