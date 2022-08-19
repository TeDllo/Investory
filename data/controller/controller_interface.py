from data.transaction import Transaction
from trade.shares.shares import Share, Action
from config.states import BotState


class Controller:
    def get_state(self, id: int) -> BotState:
        pass

    def set_state(self, id: int, state: BotState) -> None:
        pass

    def get_balance(self, id: int) -> float:
        pass

    def get_share(self, id: int) -> Share:
        pass

    def get_price(self, id: int) -> float:
        pass

    def get_operation(self, id: int) -> Transaction:
        pass

    def get_portfolio(self, id: int) -> dict[Share, int]:
        pass

    def get_portfolio_text(self, id: int) -> str:
        pass

    def accept_trade(self, id: int):
        pass

    def set_price(self, id: int, price: float):
        pass

    def set_action(self, id: int, action: Action):
        pass

    def set_quantity(self, id: int, quantity: int):
        pass

    def set_share(self, id: int, share: Share):
        pass
