from resources.generator.message.common import *
from resources.generator.message.outside import *
from resources.generator.message.user_based import *
from resources.generator.message.msg_gen import MessageGenerator

from config.states import BotState


class MessageConnector:
    def __init__(self, controller: Controller, share_core: ShareController):
        self.mapper: dict[BotState, MessageGenerator] = {
            BotState.ABOUT: AboutGenerator(),
            BotState.CHECK_LIST: CheckListGenerator(),
            BotState.HOW_TO_MAKE_PORTFOLIO: HowToMakePortfolioGenerator(),
            BotState.SHARES_CHOICE: SharesChoiceGenerator(),
            BotState.SHARES_QUANTITY: SharesQuantityGenerator(),
            BotState.START: StartGenerator(),
            BotState.TRADE_MODE: TradeModeGenerator(),
            BotState.TRADE_START: TradeStartGenerator(),
            BotState.USEFUL_INFO: UsefulGenerator(),

            BotState.SHARES_INFO: SharesInfoGenerator(controller, share_core),

            BotState.ANALYTICS: AnalyticsGenerator(),
            BotState.BALANCE: BalanceGenerator(controller),
            BotState.MY_PORTFOLIO: MyPortfolioGenerator(controller),
            BotState.SHARES_CONFIRMATION: SharesConfirmationGenerator(controller),
            BotState.SHARES_SUCCESS: SharesSuccessGenerator(controller)
        }
