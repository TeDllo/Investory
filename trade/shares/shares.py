from enum import Enum

from trade.trading import TradeSupplier

filename_rus = "trade/shares/shares_rus.txt"
filename_for = "trade/shares/shares_for.txt"


class Action(Enum):
    BUY = "Купить"
    SELL = "Продать"
    NOTHING = "Ничего"


class ShareType(Enum):
    RUSSIAN = 0
    FOREIGN = 1


class Share:
    def __init__(self, name: str, ticker: str, lot_size: int):
        self.name = name
        self.ticker = ticker
        self.lot_size = lot_size


class ShareController:
    def __init__(self, supplier: TradeSupplier):
        self.supplier = supplier
        self.shares_list: list[Share] = list()

        for share_type in ShareType:
            self.shares_list.extend(self.load_shares(share_type))

    def get_share(self, ticker: str):
        result = list(filter(lambda share: share.ticker == ticker, self.shares_list))
        if len(result) == 1:
            return result[0]
        return None

    def get_price(self, ticker: str):
        return self.supplier.get_price(ticker)

    def get_lot_size(self, ticker: str):
        return self.supplier.get_lot_size(ticker)

    def load_shares(self, type: ShareType) -> list[Share]:
        if type == ShareType.RUSSIAN:
            filename = filename_rus
        else:
            filename = filename_for

        shares_list: list[Share] = list()
        with open(filename, "r", encoding="utf-8") as shares:
            for share in shares:
                words = share.split()

                name = " ".join(words[:-1])
                ticker = words[-1]
                lot_size = self.get_lot_size(ticker)

                shares_list.append(Share(name, ticker, lot_size))

        return shares_list
