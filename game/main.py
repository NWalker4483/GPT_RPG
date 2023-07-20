
from grid import WorldGrid

class Session:
    def __init__(self) -> None:
        self.__players = []
        pass
    def is_valid_action():
        pass
    def update(self):
        for player in sorted(self.__players, key = lambda x: turn_ordering):
            valid_action = False
            while not valid_action:
                action = player.query_action()
                valid_action = self.is_valid_action(action)
        pass