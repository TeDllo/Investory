from data.controller.controller_interface import Controller
from data.types import Action, Share, Currency, Transaction
from users.user import User


class CacheController(Controller):
    def __init__(self):
        self.data: dict[int, User] = {}

    def has_user(self, id: int) -> bool:
        return id in self.data

    def add_user(self, id: int) -> None:
        self.data[id] = User(id)

    def accept_trade(self, id: int):
        operation = self.data[id].get_active_transaction()
        sign = 1 if operation.action == Action.SELL else -1

        self.data[id].balance += sign * operation.total

        if operation.share not in self.data[id].portfolio:
            self.data[id].portfolio[operation.share] = 0

        self.data[id].portfolio[operation.share] -= sign * operation.quantity * operation.share.lot_size

        if self.data[id].portfolio[operation.share] <= 0:
            self.data[id].portfolio.pop(operation.share)

    def get_balance(self, id: int, currency: Currency) -> float:
        return self.data[id].balance

    def get_share(self, id: int) -> Share:
        return self.data[id].active_share

    def get_price(self, id: int) -> float:
        return self.data[id].price

    def get_operation(self, id: int) -> Transaction:
        return self.data[id].get_active_transaction()

    def get_portfolio(self, id: int) -> dict[Share, int]:
        return self.data[id].get_portfolio()

    # def get_portfolio_text(self, id: int) -> str:
    #     text = ""
    #
    #     for share, quantity in self.get_portfolio(id).items():
    #         text += texts.portfolio_share.format(share.name, quantity)
    #
    #     if len(text) == 0:
    #         text = texts.portfolio_empty
    #
    #     return text

    def set_price(self, id: int, price: float):
        self.data[id].price = price

    def set_quantity(self, id: int, quantity: int):
        self.data[id].quantity = quantity

    def set_action(self, id: int, action: Action):
        self.data[id].action = action

    def set_share(self, id: int, share: Share):
        self.data[id].active_share = share
