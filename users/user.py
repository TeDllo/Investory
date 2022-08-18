from data.transaction import Transaction
from trade.shares.shares import Action, Share
from config.states import BotState


class User:
    def __init__(self, id: int):
        self.id = id
        self.state = BotState.START
        self.balance: float = 100000

        self.active_share = None
        self.action: Action = Action.NOTHING
        self.quantity: int = -1
        self.price: float = 0

        self.portfolio: dict[Share, int] = {}

    def get_active_transaction(self) -> Transaction:
        return Transaction(self.id, self.active_share, self.price, self.quantity, self.action)

    def get_portfolio(self) -> dict[Share, int]:
        return self.portfolio
