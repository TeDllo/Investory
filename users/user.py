from users.states import BotState

class User:
    def __init__(self, id: int):
        self.id = id
        self.state = BotState.START