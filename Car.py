class Car:
    def __init__(self, producer, color, mileage, price, classification, brakes, suspension, engine, body, gearbox,
                 loading_space):
        self.producer = producer
        self.color = color
        self.mileage = mileage
        self.price = price
        self.classification = classification
        self.brakes = brakes
        self.suspension = suspension
        self.engine = engine
        self.body = body
        self.gearbox = gearbox
        self.loading_space = loading_space

    def __repr__(self):
        return f''
