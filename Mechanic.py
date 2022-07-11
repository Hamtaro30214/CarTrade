from Player import Player


class Mechanic(Player):
    def __init__(self, name, chance):
        super().__init__()
        self.name = name
        self.chance = chance

    def __repr__(self):
        return f"{self.name}, {int(self.chance * 100)}%"
