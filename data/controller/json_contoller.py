import json
from typing import Any

from data.controller.controller_interface import Controller
from data.types import Currency, Position, Action, Transaction
from trade.shares.shares import Share, ShareController

INDENT = 2


def create_user(id: int) -> dict:
    return {
        id: {
            "balance_rub": 100000,
            "balance_usd": 0,

            "chosen_share": "",
            "chosen_price": 0,
            "chosen_action": "Ничего",
            "chosen_quantity": 0.0,

            "portfolio": {}
        }
    }


def create_position() -> dict:
    return {
        "quantity": 0,
        "total": 0.0
    }


class JSONController(Controller):
    def __init__(self, filepath, share_controller: ShareController):
        self.filename = filepath
        self.share_core = share_controller

    def has_user(self, id: int) -> bool:
        with open(self.filename, "r") as user_db:
            return str(id) in json.load(user_db)

    def add_user(self, id: int) -> None:
        with open(self.filename, "r+") as user_db:
            source: dict = json.load(user_db)
            source.update(create_user(id))
            user_db.seek(0)
            json.dump(source, user_db, indent=INDENT)
            user_db.truncate()

    def get_balance(self, id: int, currency: Currency) -> float:
        with open(self.filename, "r") as user_db:
            source: dict = json.load(user_db)
            return source[str(id)]["balance_" + currency.value.lower()]

    def get_share(self, id: int) -> Share:
        with open(self.filename, "r") as user_db:
            source: dict = json.load(user_db)
            ticker = source[str(id)]["chosen_share"]
            return Share(
                self.share_core.get_name(ticker),
                ticker,
                self.share_core.get_lot_size(ticker),
                self.share_core.get_currency(ticker)
            )

    def get_price(self, id: int) -> float:
        with open(self.filename, "r") as user_db:
            source: dict = json.load(user_db)
            return source[str(id)]["chosen_price"]

    def get_operation(self, id: int) -> Transaction:
        with open(self.filename, "r") as user_db:
            source: dict = json.load(user_db)
            return Transaction(id,
                               self.get_share(id),
                               self.get_price(id) * source[str(id)]["chosen_quantity"],
                               source[str(id)]["chosen_quantity"],
                               Action(source[str(id)]["chosen_action"]))

    def get_portfolio(self, id: int) -> list[Position]:
        with open(self.filename, "r") as user_db:
            source: dict = json.load(user_db)
            position_dict: dict = source[str(id)]["portfolio"]
            result: list[Position] = list()

            for ticker, position_obj in position_dict.items():
                result.append(Position(
                    self.share_core.get_share(ticker),
                    position_obj["quantity"],
                    position_obj["total"]
                ))

            return result

    def accept_trade(self, id: int):
        op = self.get_operation(id)

        with open(self.filename, "r+") as user_db:
            source: dict = json.load(user_db)
            portfolio: dict = source[str(id)]["portfolio"]

            if op.share.ticker not in portfolio:
                portfolio[op.share.ticker] = create_position()

            position = portfolio[op.share.ticker]

            sign = 1
            if op.action == Action.SELL:
                sign = -1

            position["quantity"] += sign * op.quantity
            position["total"] += sign * op.total

            if position["quantity"] == 0:
                portfolio.pop(op.share.ticker)

            source[str(id)]["balance_" + op.share.currency.lower()] -= sign * op.total

            user_db.seek(0)
            json.dump(source, user_db, indent=INDENT)
            user_db.truncate()

    def set_chosen_field(self, id: int, field: str, value: Any):
        with open(self.filename, "r+") as user_db:
            source: dict = json.load(user_db)
            source[str(id)][field] = value
            user_db.seek(0)
            json.dump(source, user_db, indent=INDENT)
            user_db.truncate()

    def set_price(self, id: int, price: float):
        self.set_chosen_field(id, "chosen_price", price)

    def set_share(self, id: int, share: Share):
        self.set_chosen_field(id, "chosen_share", share.ticker)

    def set_quantity(self, id: int, quantity: int):
        self.set_chosen_field(id, "chosen_quantity", quantity * self.share_core.get_lot_size(self.get_share(id).ticker))

    def set_action(self, id: int, action: Action):
        self.set_chosen_field(id, "chosen_action", action.value)
