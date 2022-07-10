import random
from Car import Car

PRODUCERS = ("Ford", "Opel", "Volkswagen", "Audi")
COLORS = ('White', 'Blue', 'Red', 'Black', 'Yellow')
CLASSIFICATIONS = ("Budget", "Standard", "Premium")


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

    def generate_car(self):
        self.garage.append(Car(random.choice(PRODUCERS), round(random.uniform(500, 1000), 2), random.choice(COLORS),
                               random.randint(20000, 300000), random.choice(CLASSIFICATIONS),
                               bool(random.getrandbits(1)),
                               bool(random.getrandbits(1)), bool(random.getrandbits(1)), bool(random.getrandbits(1)),
                               bool(random.getrandbits(1)), random.randint(15, 100)))

    @staticmethod
    def bigger(pla, num):
        return pla > num

    def start_game(self, player):
        if not any([car.price < player.money for car in self.garage]):
            raise ValueError("Player can't afford any car")
