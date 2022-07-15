import random

import Constants


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

    def menu(self):
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

    def buy(self, market, index):
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
        print([car.brakes, car.suspension, car.engine, car.brakes, car.gearbox].count(False), client.destroyed)
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

    def show_parts(self, car_index):
        print(f'Suspension:{self.garage[car_index].parts[0]}, Engine:{self.garage[car_index].parts[1]}, '
              f'Brakes:{self.garage[car_index].parts[2]}, Body:{self.garage[car_index].parts[3]}, '
              f'Gearbox:{self.garage[car_index].parts[4]}')

    def repair(self, car_index, part, mechanic):
        # calculate cost of part based on: type, classification, producer of car and repair cost of mechanic
        cost_of_part = Constants.PARTS_BY_INDEX.get(part) * \
                       Constants.COST_CLASSIFICATIONS.get(self.garage[car_index].classification) * \
                       Constants.COST_PRODUCERS.get(self.garage[car_index].producer) * mechanic.repair_cost
        if cost_of_part > self.money:
            raise ValueError("You don't have enough money to repair this part")
        another_part = ''
        if not random.random() < mechanic.chance:
            if mechanic.name == 'Andrew':
                if random.random() > 0.02 and self.garage[car_index].parts.count(True) > 1:
                    for index, item in enumerate(self.garage[car_index].parts):
                        if item and part != index:
                            self.garage[car_index].parts[index] = False
                            break
                    another_part = 'and he destroyed another part'
            return f'Mechanic could not repair the part {another_part}'
        # success transaction
        self.money -= cost_of_part
        self.garage[car_index].parts[part] = True
        print(f'You repaired one part and you have {self.garage[car_index].parts.count(False)} parts to repair')
