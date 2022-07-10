class Player:
    def __init__(self):
        self._money = 2000.0
        self.garage = []

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, cash):
        self._money = cash
