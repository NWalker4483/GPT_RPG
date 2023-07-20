from grid import WorldGrid

class Session:
    def __init__(self) -> None:
        self.__players = []
        self.world = WorldGrid()
    def is_valid_action():
        pass
    def update(self):
        # Check for prompt updates
        for player in sorted(self.__players, key = lambda x: turn_ordering):
            valid_action = False
            while not valid_action:
                action = player.query_action()
                valid_action = self.is_valid_action(action)
            apply_effects()
        pass
    def run(self):
        pass
if __name__ == "__main__":
    pass