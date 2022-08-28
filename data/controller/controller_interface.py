from data.types import Currency, Position, Transaction, Share, Action


class Controller:
    def has_user(self, id: int) -> bool:
        pass

    def add_user(self, id: int) -> None:
        pass

    def get_balance(self, id: int, currency: Currency) -> float:
        pass

    def get_share(self, id: int) -> Share:
        pass

    def get_price(self, id: int) -> float:
        pass

    def get_operation(self, id: int) -> Transaction:
        pass

    def get_portfolio(self, id: int) -> list[Position]:
        pass

    def get_currency_quantity(self, id: int) -> float:
        pass

    def get_currency(self, id: int) -> Currency:
        pass

    def get_currency_price(self, id: int) -> float:
        pass

    def accept_trade(self, id: int):
        pass

    def accept_exchange(self, id: int):
        pass

    def set_price(self, id: int, price: float):
        pass

    def set_action(self, id: int, action: Action):
        pass

    def set_quantity(self, id: int, quantity: int):
        pass

    def set_share(self, id: int, share: Share):
        pass

    def set_currency_quantity(self, id: int, quantity: float):
        pass

    def set_currency(self, id: int, currency: Currency):
        pass

    def set_currency_price(self, id: int, price: float):
        pass
