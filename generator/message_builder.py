from users.states import BotState
from users.controller.controller_interface import Controller
from resources import messages


class MessageGenerator:
    def __init__(self, controller: Controller):
        self.controller = controller

    def generate_message(self, state: BotState, id: int) -> str:
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


class MessageBuilder:
    def __init__(self, controller: Controller):
        self.generator = MessageGenerator(controller)

    def get_message(self, state: BotState, id=0) -> str:
        return self.generator.generate_message(state, id)
