from resources.generator.message.common import *
from resources.generator.message.outside import *
from resources.generator.message.user_based import *
from resources.generator.message.msg_gen import MessageGenerator

from config.states import BotState


class MessageConnector:
    def __init__(self, controller: Controller, share_core: ShareController):
        balance_generator = BalanceGenerator(controller)

        self.mapper: dict[BotState, MessageGenerator] = {
            BotState.ABOUT: AboutGenerator(),
            BotState.CHECK_LIST: CheckListGenerator(),
            BotState.HOW_TO_MAKE_PORTFOLIO: HowToMakePortfolioGenerator(),
            BotState.SHARES_CHOICE: SharesChoiceGenerator(share_core),
            BotState.SHARES_QUANTITY: SharesQuantityGenerator(),
            BotState.START: StartGenerator(),
            BotState.TRADE_MODE: TradeModeGenerator(),
            BotState.TRADE_START: TradeStartGenerator(),
            BotState.USEFUL_INFO: UsefulGenerator(),

            BotState.SHARES_INFO: SharesInfoGenerator(controller, share_core),

            BotState.ANALYTICS: AnalyticsGenerator(),
            BotState.BALANCE: balance_generator,
            BotState.MY_PORTFOLIO: MyPortfolioGenerator(controller),
            BotState.SHARES_CONFIRMATION: SharesConfirmationGenerator(controller),
            BotState.SHARES_SUCCESS: SharesSuccessGenerator(controller),
            BotState.SHARES_CURRENCY_OFFER: SharesCurrencyOfferGenerator(controller),

            BotState.EXCHANGE: ExchangeGenerator(share_core),
            BotState.EXCHANGE_QUANTITY: ExchangeQuantityGenerator(controller),
            BotState.EXCHANGE_CONFIRMATION: ExchangeConfirmationGenerator(controller),
            BotState.EXCHANGE_SUCCESS: ExchangeSuccessGenerator(balance_generator)
        }
