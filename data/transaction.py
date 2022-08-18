from trade.shares.shares import Share, Action


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
