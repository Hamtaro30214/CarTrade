import random

import Constants
from Car import Car
from Client import Client
from Mechanic import Mechanic
from Player import Player

player = Player()
market = [Car() for _ in range(random.randint(3, 7))]
player.start_game(market)
clients = [Client(), Client(), Client()]
mechanics = [Mechanic('Janus', 1, 1.5), Mechanic('Marian', 0.9, 1), Mechanic('Andrew', 0.8, 0.7)]
TARGET = player.money * 2
player.garage.append(market[0])
while True:
    player.main_menu()
    main_menu_input = int(input('Type number from main menu: '))
    match main_menu_input:
        case 1:
            while player.money < TARGET:
                player.menu()
                menu_choose = int(input('Type number from game menu: '))
                match menu_choose:
                    case 1:
                        if not player.token:
                            print('Not available  int this turn')
                        else:
                            print([(car, market[car]) for car in range(len(market))])
                            car_index = int(input('Enter the index of the car you want to buy: '))
                            if car_index < len(market):
                                if player.buy(market[car_index]):
                                    market.remove(market[car_index])
                                    market.extend([Car(), Car()])
                            else:
                                print('There is no car on the market with the given index.')
                    case 2:
                        print(player.sell(clients))
                    case 3:
                        print(player.repair_part(mechanics))
                    case 4:
                        if not player.token:
                            print('Not available  int this turn')
                        else:
                            player.show_ads()
                            ad_index = int(input('Choose one of the forms of advertising: '))
                            if 0 <= ad_index <= 2:
                                if not player.can_afford(Constants.AD_COST.get(ad_index)):
                                    print("You can't afford the ad")
                                else:
                                    new_clients = player.buy_ad(ad_index)
                                    for _ in range(new_clients):
                                        clients.append(Client())
                                    print(f'You gain {new_clients} clients.')
                            else:
                                print("You didn't select an ad.")
                    case 5:
                        print([(car, market[car]) for car in range(len(market))])
                    case 6:
                        if not player.garage:
                            print("You don't have any car")
                        else:
                            print(player.garage)
                    case 7:
                        print([(person, clients[person]) for person in range(len(clients))])
                    case 8:
                        print(player.money)
                    case 9:
                        if not player.transactions:
                            print("You don't have reported transaction history")
                        else:
                            print(player.transactions)
                    case 10:
                        if not player.repair_part:
                            print("You don't have repair history")
                        else:
                            print(player.repair_history)
                    case 11:
                        player.token = True
                    case 12:
                        break
                    case _:
                        print('Selected number not in menu')
            else:
                print(f'You won the game in {player.moves}, washed {player.wash_the_car} times.')
        case 2:
            print('The goal of the game is to double your starting cash in as few moves as possible.'
                  ' One move is to buy a car / sell a car / fix one item / add one ad. Viewing your account balance,'
                  ' transaction history, customer databases, vehicles owned and vehicles available for purchase does'
                  ' not imply using move.')
        case 3:
            break
        case _:
            print('Selected number not in menu')
