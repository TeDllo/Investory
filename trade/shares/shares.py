from enum import Enum

filename_rus = "trade/shares/shares_rus.txt"
filename_for = "trade/shares/shares_for.txt"


class Action(Enum):
    BUY = "Купить"
    SELL = "Продать"
    NOTHING = "Ничего"


class Share:
    def __init__(self, name: str, ticker: str):
        self.name = name
        self.ticker = ticker


class ShareController:
    def __init__(self):
        self.shares_list: list[Share] = list()

        for share_type in ShareType:
            self.shares_list.extend(get_shares(share_type))

    def get_share(self, ticker: str):
        result = list(filter(lambda share: share.ticker == ticker, self.shares_list))
        if len(result) == 1:
            return result[0]
        return None

    def get_price(self, ticker: str):
        return 100

class ShareType(Enum):
    RUSSIAN = 0
    FOREIGN = 1


def get_shares(type: ShareType) -> list[Share]:
    if type == ShareType.RUSSIAN:
        filename = filename_rus
    else:
        filename = filename_for

    shares_list: list[Share] = list()
    with open(filename, "r", encoding="utf-8") as shares:
        for share in shares:
            words = share.split()
            shares_list.append(Share(" ".join(words[:-1]), words[-1]))
    return shares_list
