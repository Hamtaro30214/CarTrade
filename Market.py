import random
import Constants

from Car import Car


class Market:
    def __init__(self):
        self.car_shelter = []

    def generate_car(self):
        self.car_shelter.append(Car(random.choice(Constants.PRODUCERS), round(random.uniform(500, 1000), 2),
                                    random.choice(Constants.COLORS), random.randint(20000, 300000),
                                    random.choice(Constants.CLASSIFICATIONS), bool(random.getrandbits(1)),
                                    bool(random.getrandbits(1)), bool(random.getrandbits(1)),
                                    bool(random.getrandbits(1)),
                                    bool(random.getrandbits(1)), random.randint(15, 100)))

    def show_basic_info(self):
        for car in self.car_shelter:
            print(f'{car.price}, {car.producer}, {car.classification},'
                  f' {[car.brakes, car.suspension, car.engine, car.engine, car.gearbox].count(False)}')
