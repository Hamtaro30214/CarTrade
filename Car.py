import random
import Constants


class Car:
    def __init__(self):
        self.producer = random.choice(Constants.PRODUCERS)
        self.price = round(random.uniform(500, 1000), 2)
        self.color = random.choice(Constants.COLORS)
        self.mileage = random.randint(20000, 300000)
        self.classification = random.choice(Constants.CLASSIFICATIONS)
        self.parts = [bool(random.getrandbits(1)) for _ in range(5)]
        self.loading_space = random.randint(15, 100)

    # self.car_shelter.append(Car(random.choice(Constants.PRODUCERS), round(random.uniform(500, 1000), 2),
    #                             random.choice(Constants.COLORS), random.randint(20000, 300000),
    #                             random.choice(Constants.CLASSIFICATIONS),
    #                             [bool(random.getrandbits(1)) for _ in range(5)], random.randint(15, 100)))
    def __repr__(self):
        if self.loading_space > 60:
            type_of_vehicle = 'Van'
        else:
            type_of_vehicle = 'Car'
        return f'{type_of_vehicle}({self.producer}, {self.price}, {self.color}, {self.mileage}, {self.classification},'\
               f' {self.parts})'
