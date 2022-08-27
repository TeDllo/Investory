from enum import Enum

from tinvest import Currency


class Action(Enum):
    BUY = "Купить"
    SELL = "Продать"
    NOTHING = "Ничего"


class Share:
    def __init__(self, name: str, ticker: str, lot_size: int, currency: Currency):
        self.name = name
        self.ticker = ticker
        self.lot_size = lot_size
        self.currency = currency


class Position:
    def __init__(self, share: Share, quantity: int, total: float):
        self.share = share
        self.quantity = quantity
        self.total = total


class Transaction:
    def __init__(self,
                 user_id: int,
                 share: Share,
                 price: float,
                 quantity: int,
                 action: Action):
        self.user_id = user_id
        self.share = share
        self.price = price
        self.quantity = quantity
        self.action = action
