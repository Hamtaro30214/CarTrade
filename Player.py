import random

import Constants


class Player:
    def __init__(self, money=3000.0):
        self._money = money
        self.garage = []
        self.token = True
        self.moves = 0
        self.wash_the_car = 0
        self.transactions = []
        self.repair_history = []

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, cash):
        self._money = cash

    def menu(self):
        if self.token:
            print('==============MENU==============')
            print('Choose 1 to buy a car.')
            print('Choose 2 to sell a car.')
            print('Choose 3 to repair a part.')
            print('Choose 4 to buy an ad.')
            print('Choose 5 to view the car market.')
            # print("Choose 6 to view the market with basic info.")
            print('Choose 6 to view full info about your cars.')
            print('Choose 7 to view clients.')
            # print('Choose 9 to view ads.')
            print('Choose 8 to view your balance.')
            print('Select 9 to check transaction history.')
            print('Select 10 to check repair history')
            print('Choose 11 to end turn.')
            print('Choose 12 to exit.')
        else:
            print('==============MENU==============')
            print('Choose 5 to view the car market.')
            print('Choose 6 to view full info about your cars.')
            print('Choose 7 to view clients.')
            print('Choose 8 to view your balance.')
            print('Select 9 to check transaction history.')
            print('Select 10 to check repair history')
            print('Choose 11 to end turn.')
            print('Choose 12 to exit.')

    def start_game(self, market):
        if not any([car.price < self.money for car in market]):
            raise ValueError("Player can't afford any car")

    def move(self):
        self.moves += 1
        self.token = False

    def buy(self, car):
        """Method allow buying a car from market
        car: a car from list market
        """
        if not self.token:
            return "You can't use it in this turn"
        if self.money < car.price:
            print('Not enough money for the car 💰')
            return False
        self.money -= car.price + car.price * 0.02
        self.garage.append(car)
        self.wash_the_car += 1
        self.move()
        print('You bought the car 🚗')
        return True

    def sell(self, clients):
        """Method gets from player index of car to sell, index of customer he is willing to buy the car
        """
        if not self.token:
            return "You can't use it in this turn"
        print([(car, self.garage[car]) for car in range(len(self.garage))])
        car_index = int(input('Enter the index of the car you want to sell: '))
        if car_index > len(self.garage) or not self.garage:
            return "You don't have a car at given position"
        print([(person, clients[person]) for person in range(len(clients))])
        client_index = int(input('Enter the index of the customer you want to sell the car to: '))
        if car_index > len(clients):
            return 'Invalid index of client'
        car = self.garage[car_index]
        client = clients[client_index]
        if car.price > client.money:
            return 'The customer cannot afford this car.'
        if car.producer not in client.producers:
            return 'The customer does not accept the car of this producer.'
        if client.type_of_vehicle == 'Van' and car.loading_space < 60 or\
                client.type_of_vehicle == 'Car' and car.loading_space > 60:
            return 'The customer does not accept the car of this type.'
        if car.parts.count(False) != 0:
            if not client.suspension:
                return "The customer don't accept car with broken suspension"
            if not client.destroyed:
                return "The customer don't accept destroyed cars"
        self.garage.remove(car)
        client.money -= car.price + car.price * 0.02
        self.money += car.price - car.price * 0.02
        self.move()
        self.wash_the_car += 1
        self.transactions.append((car, client))
        print('The car was successfully sold')

    @staticmethod
    def show_parts(car):
        print(f'0. Suspension:{car.parts[0]}, 1. Engine:{car.parts[1]}, '
              f'2. Brakes:{car.parts[2]}, 3. Body:{car.parts[3]}, '
              f'4. Gearbox:{car.parts[4]}')

    def repair_part(self, mechanics):
        """
        First check user inputs if are valid
        After input calculate cost of part based on: type, classification, producer of car and repair cost of mechanic
        Later try to repair the part with a mechanic's chance
        If everything is correct repair the part
        """
        print([(car, self.garage[car]) for car in range(len(self.garage))])
        car_index = int(input('Enter the index of the car you want to repair: '))
        if car_index > len(self.garage) or not self.garage:
            return "You don't have a car at given position"
        car = self.garage[car_index]
        self.show_parts(car)
        part_index = int(input('Enter the index of the part you want to repair: '))
        if car.parts[part_index]:
            return 'Part is already repaired'
        print([(num, mechanics[num]) for num in range(3)])
        mechanic_index = int(input('Choose one of mechanics with different chance to repair a part: '))
        mechanic = mechanics[mechanic_index]
        part_cost = Constants.PARTS_BY_INDEX.get(part_index) * Constants.COST_CLASSIFICATIONS.get(car.classification) \
                    * Constants.COST_PRODUCERS.get(car.producer) * mechanic.repair_cost
        if part_cost > self.money:
            return "You don't have enough money to repair this part"
        another_part = ''
        if not random.random() < mechanic.chance:
            if mechanic.name == 'Andrew':
                if random.random() > 0.02 and car.parts.count(True) > 1:
                    for index, item in enumerate(car.parts):
                        if item and part_index != index:
                            car.parts[index] = False
                            break
                    another_part = 'and he destroyed another part'
            return f'Mechanic could not repair the part {another_part}'
        self.move()
        self.money -= part_cost
        car.parts[part_index] = True
        car.price += car.price * Constants.PARTS_INCREASE_VALUE.get(part_index)
        self.repair_history.append((car, part_cost, mechanic))
        return f'You repaired one part and you have {self.garage[car_index].parts.count(False)} parts to repair'

    @staticmethod
    def show_ads():
        print('Select 0 to buy marketing campaign for $400 and gain 2 clients\n'
              'Select 1 to buy an ad in your local  newspaper for $400 and gain 1-3 clients\n'
              'Select 2 to buy online ad for $200 and gain 1 client')

    def can_afford(self, ad_cost):
        return self.money > ad_cost

    def buy_ad(self, ad):
        self.move()
        if ad == 0:
            self.money -= 400
            return 2
        if ad == 1:
            self.money -= 300
            return random.randint(1, 3)
        self.money -= 200
        return 1

    @staticmethod
    def main_menu():
        print('Welcome to the game Car Trade.\n'
              'Select 1 to play.\n'
              'Select 2 for the rules of the game.\n'
              'Select 3 to exit.')
