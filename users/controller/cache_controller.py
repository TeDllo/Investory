from users.controller.controller_interface import Controller
from users.states import BotState
from users.user import User


class CacheController(Controller):
    def __init__(self):
        self.data: dict[int, User] = {}

    def add_user(self, id: int) -> None:
        self.data[id] = User(id)

    def get_state(self, id: int) -> BotState:
        if id not in self.data:
            return BotState.NOT_STARTED
        return self.data[id].state

    def set_state(self, id: int, state: BotState) -> None:
        self.data[id].state = state
