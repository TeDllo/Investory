from data.types import Transaction, Action, Share


class User:
    def __init__(self, id: int):
        self.id = id
        self.balance: float = 100000

        self.active_share = None
        self.action: Action = Action.NOTHING
        self.quantity: int = -1
        self.price: float = 0

        self.portfolio: dict[Share, int] = {}

    def get_active_transaction(self) -> Transaction:
        return Transaction(
            user_id=self.id,
            share=self.active_share,
            total=round(self.price * self.quantity * self.active_share.lot_size, 2),
            quantity=self.quantity,
            action=self.action
        )

    def get_portfolio(self) -> dict[Share, int]:
        return self.portfolio
