from config.states import BotState
from data.data_handlers import *


class DataHandlersCore:
    def __init__(self, controller: Controller, share_core: ShareController):
        self.mapper: dict[BotState, DataHandler] = {
            BotState.SHARES_CHOICE: SharesChoiceHandler(controller, share_core),
            BotState.SHARES_INFO: SharesInfoHandler(controller),
            BotState.SHARES_QUANTITY: SharesQuantityHandler(controller),
            BotState.SHARES_CONFIRMATION: SharesConfirmationHandler(controller, share_core)
        }