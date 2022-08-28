from data.types import Share, Currency
from trade.trading import TradeSupplier

filename_rus = "trade/shares/shares_rus.txt"
filename_for = "trade/shares/shares_for.txt"


class ShareController:
    def __init__(self, supplier: TradeSupplier):
        self.supplier = supplier
        self.shares_list: list[Share] = list()

        self.shares_list.extend(self.load_shares(Currency.rub))
        self.shares_list.extend(self.load_shares(Currency.usd))

    def get_share(self, ticker: str):
        result = list(filter(lambda share: share.ticker == ticker, self.shares_list))
        if len(result) == 1:
            return result[0]
        new_share = Share(
            self.get_name(ticker),
            ticker,
            self.get_lot_size(ticker),
            self.get_currency(ticker)
        )
        self.shares_list.append(new_share)
        return new_share

    def get_name(self, ticker: str):
        return self.supplier.get_name(ticker)

    def get_price(self, ticker: str):
        return self.supplier.get_price(ticker)

    def get_lot_size(self, ticker: str):
        return self.supplier.get_lot_size(ticker)

    def get_currency(self, ticker: str) -> Currency:
        return self.supplier.get_currency(ticker)

    def exists(self, ticker: str) -> bool:
        return self.supplier.exists(ticker)

    def load_shares(self, currency: Currency) -> list[Share]:
        if currency == Currency.rub:
            filename = filename_rus
        else:
            filename = filename_for

        shares_list: list[Share] = list()
        with open(filename, "r", encoding="utf-8") as shares:
            for share in shares:
                words = share.split()

                name = " ".join(words[:-1])
                ticker = words[-1][1:]
                lot_size = self.get_lot_size(ticker)

                shares_list.append(Share(name, ticker, lot_size, currency))

        return shares_list
