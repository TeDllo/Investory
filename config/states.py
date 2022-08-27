from enum import Enum


class BotState(Enum):
    NOT_IMPLEMENTED = -2

    NOT_STARTED = -1
    START = 0

    TRADE_MODE = 1
    MY_PORTFOLIO = 2
    BALANCE = 3
    ANALYTICS = 4
    TRADE_START = 5

    SHARES_CHOICE = 6
    SHARES_INFO = 7
    SHARES_QUANTITY = 8
    SHARES_CONFIRMATION = 9
    SHARES_CURRENCY_OFFER = 15
    SHARES_SUCCESS = 10

    USEFUL_INFO = 11
    HOW_TO_MAKE_PORTFOLIO = 12
    CHECK_LIST = 13

    ABOUT = 14
