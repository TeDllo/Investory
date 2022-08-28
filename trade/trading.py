import tinvest

from data.types import Currency


class TradeCore:
    def __init__(self, token: str):
        self.client = tinvest.SyncClient(token=token, use_sandbox=True)

    def get_instrument_by_ticker(self, ticker: str):
        response = self.client.get_market_search_by_ticker(ticker)
        return response.payload.instruments[0]

    def get_lot_by_ticker(self, ticker: str) -> int:
        return self.get_instrument_by_ticker(ticker).lot

    def get_figi_by_ticker(self, ticker: str) -> str:
        return self.get_instrument_by_ticker(ticker).figi

    def get_price_by_figi(self, figi: str) -> float:
        response = self.client.get_market_orderbook(figi=figi, depth=1)
        return float(response.payload.last_price)

    def get_price_by_ticker(self, ticker: str) -> float:
        price = self.get_price_by_figi(self.get_figi_by_ticker(ticker))
        return round(price, 2)

    def get_name_by_ticker(self, ticker: str) -> str:
        return self.get_instrument_by_ticker(ticker).name

    def get_currency_by_ticker(self, ticker: str) -> Currency:
        return self.get_instrument_by_ticker(ticker).currency

    def exists_by_ticker(self, ticker: str) -> bool:
        return len(self.client.get_market_search_by_ticker(ticker).payload.instruments) > 0


class TradeSupplier:
    def __init__(self, core: TradeCore):
        self.core = core

    def get_name(self, ticker: str) -> str:
        return self.core.get_name_by_ticker(ticker)

    def get_price(self, ticker: str) -> float:
        return self.core.get_price_by_ticker(ticker)

    def get_lot_size(self, ticker: str) -> int:
        return self.core.get_lot_by_ticker(ticker)

    def get_currency(self, ticker: str) -> Currency:
        return self.core.get_currency_by_ticker(ticker)

    def get_currency_price(self, currency: Currency) -> float:
        if currency == Currency.usd:
            return self.get_price("USD000UTSTOM")

    def exists(self, ticker: str) -> bool:
        return self.core.exists_by_ticker(ticker)
