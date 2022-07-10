class Car:
    def __init__(self, producer, price, color, mileage, classification, brakes, suspension, engine, body, gearbox,
                 loading_space):
        self.producer = producer
        self.price = price
        self.color = color
        self.mileage = mileage
        self.classification = classification
        self.brakes = brakes
        self.suspension = suspension
        self.engine = engine
        self.body = body
        self.gearbox = gearbox
        self.loading_space = loading_space

    def __repr__(self):
        if self.loading_space > 60:
            type_of_vehicle = 'Van'
        else:
            type_of_vehicle = 'Car'
        return f'{type_of_vehicle}({self.producer}, {self.price}, {self.color}, {self.mileage}, {self.classification},'\
               f' {self.brakes}, {self.suspension}, {self.engine}, {self.body}, {self.gearbox})'
