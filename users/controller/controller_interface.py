from users.states import BotState


class Controller:
    def add_user(self, id: int) -> None:
        pass

    def get_state(self, id: int) -> BotState:
        pass

    def set_state(self, id: int, state: BotState) -> None:
        pass

    def get_balance(self, id: int) -> int:
        pass
