class Player:
    def __init__ (self, money=2000.0):
        self._money = money
        self.garage = []
        self.token = True
        self.moves = 0
        self.wash_the_car = 0

    @property
    def money (self):
        return self._money

    @money.setter
    def money (self, cash):
        self._money = cash

    def menu (self):
        if self.token:
            print('==============MENU==============')
            print('Choose 1 to buy a car.')
            print('Choose 2 to sell a car.')
            print('Choose 3 to repair a part.')
            print('Choose 4 to buy an ad.')
            print('Choose 5 to view the car market.')
            print("Choose 6 to view the market with basic info.")
            print('Choose 7 to view full info about your cars.')
            print('Choose 8 to view clients.')
            print('Choose 9 to view ads.')
            print('Choose 10 to view your balance.')
            print('Choose 11 to end turn.')
            print('Choose 13 to exit.')
            print('==============MENU==============')
        else:
            print('==============MENU==============')
            print('Choose 1 to view the car market')
            print("Choose 3 to view your cars with basic info.")
            print('Choose 4 to view full info about cars ')
            print('Choose 7 to view ads')
            print('Choose 11 to view your balance')
            print('Choose 12 to end turn')
            print('Choose 13 to exit')

    def start_game (self, market):
        if not any([car.price < self.money for car in market]):
            raise ValueError("Player can't afford any car")

    def buy (self, market, index):
        if self.money < market[index].price:
            raise ValueError('Not enough money for the car 💰')
        self.money -= market[index].price + market[index].price * 0.02
        self.garage.append(market[index])
        market.remove(market[index])
        self.wash_the_car += 1
        print('You bought the car 🚗')

    def move (self):
        self.moves += 1
        self.token = False

    def sell (self, car, client):
        if car.price > client.money:
            raise ValueError('The customer cannot afford this car')
        if car.producer not in client.type_of_vehicle:
            raise ValueError('The customer does not accept the car of this producer')
        print([car.brakes, car.suspension, car.engine, car.engine, car.gearbox].count(False), client.destroyed)
        if [car.brakes, car.suspension, car.engine, car.engine, car.gearbox].count(False) != 0:
            if not client.suspension:
                raise ValueError("The customer don't accept car with broken suspension")
            if not client.destroyed:
                raise ValueError("The customer don't accept destroyed cars")
        self.garage.remove(car)
        client.garage.append(car)
        client.money -= car.price + car.price * 0.02
        self.money += car.price - car.price * 0.02
        self.move()
        self.wash_the_car += 1
        print('The car was successfully sold')

    def show_parts(self, pos):
        print(f'Brakes:{self.garage[pos].brakes}, Suspension:{self.garage[pos].suspension}, '
              f'Engine:{self.garage[pos].engine}, Body:{self.garage[pos].body}, Gearbox:{self.garage[pos].gearbox}')


