class Car:
    def __init__(self, producer, price, color, mileage, classification, parts,
                 loading_space):
        self.producer = producer
        self.price = price
        self.color = color
        self.mileage = mileage
        self.classification = classification
        self.parts = parts
        self.loading_space = loading_space

    def __repr__(self):
        if self.loading_space > 60:
            type_of_vehicle = 'Van'
        else:
            type_of_vehicle = 'Car'
        return f'{type_of_vehicle}({self.producer}, {self.price}, {self.color}, {self.mileage}, {self.classification},'\
               f' {self.parts})'
