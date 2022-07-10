class Player:
    def __init__(self, money=2000.0):
        self._money = money
        self.garage = []
        self.token = True

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

    def start_game(self, market):
        if not any([car.price < self.money for car in market]):
            raise ValueError("Player can't afford any car")

    def buy(self, market, index):
        if self.money < market[index].price:
            raise ValueError('Not enough money for the car 💰')
        self.money -= market[index].price
        self.garage.append(market[index])
        market.remove(market[index])
        print('You bought the car 🚗')
