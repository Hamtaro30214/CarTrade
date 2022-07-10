import random
from Car import Car


class Player:
    def __init__(self, money=2000.0):
        self._money = money
        self.garage = []
    PRODUCERS = ("Ford", "Opel", "Volkswagen", "Audi")
    COLORS = ('White', 'Blue', 'Red', 'Black', 'Yellow')
    CLASSIFICATIONS = ("Budget", "Standard", "Premium")

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, cash):
        self._money = cash

    def generate_car(self):
        self.garage.append(Car(random.choice(Player.PRODUCERS), round(random.uniform(500, 1000), 2),
                               random.choice(Player.COLORS), random.randint(20000, 300000),
                               random.choice(Player.CLASSIFICATIONS), bool(random.getrandbits(1)),
                               bool(random.getrandbits(1)), bool(random.getrandbits(1)), bool(random.getrandbits(1)),
                               bool(random.getrandbits(1)), random.randint(15, 100)))

    def start_game(self, player):
        if not any([car.price < player.money for car in self.garage]):
            raise ValueError("Player can't afford any car")
