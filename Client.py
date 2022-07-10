import random

from Player import Player
import Constants


class Client(Player):
    def __init__(self, money=round(random.uniform(500, 1000), 2)):
        super().__init__(money)
        self.producers = random.sample(Constants.PRODUCERS, 2)
        self.type_of_vehicle = random.choice(['Van', 'Car'])
        self.suspension = random.random() > 0.7
        self.destroyed = random.random() > 0.9

    def __repr__(self):
        return f'Client({self.money}, {self.producers}, {self.type_of_vehicle}, {self.suspension}, {self.destroyed})'
