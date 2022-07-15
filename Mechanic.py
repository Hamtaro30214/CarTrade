from Player import Player


class Mechanic(Player):
    def __init__(self, name, chance, repair_cost):
        super().__init__()
        self.name = name
        self.chance = chance
        self.repair_cost = repair_cost

    def __repr__(self):
        return f"{self.name}, {int(self.chance * 100)}%, {self.repair_cost}"
