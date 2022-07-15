import math
import random
from Client import Client
from Market import Market
from Mechanic import Mechanic
from Player import Player
import Constants


player = Player()
market = Market()
for _ in range(random.randint(3, 7)):
    market.generate_car()
player.start_game(market.car_shelter)
clients = []
for _ in range(3):
    clients.append(Client())
target = player.money * 2
player.garage.append(market.car_shelter[1])
print(market.car_shelter[1])

chosen_client = 3

if chosen_client < 0 or chosen_client > 14:
    raise ValueError('Invalid number')
player.menu()
mechanics = [Mechanic('Janus', 1, 1.5), Mechanic('Marian', 0.9, 1), Mechanic('Andrew', 0.8, 0.7)]
# TODO: case 5 and 8 one function to print all objects from list
match chosen_client:
    case 1:
        player.buy(market.car_shelter, 0)
        player.move()
    case 2:
        # car_index = int(input('Enter the index of the car you want to sell: '))
        # if len(player.garage) < car_index:
        #     raise IndexError("You don't have a car at given position")
        # client_index = int(input('Enter the index of the customer you want to sell the car to: '))
        car_index = client_index = 0
        player.sell(player.garage[car_index], clients[client_index])
    case 3:
        car_index = int(input('Enter the index of the car you want to repair: '))
        if len(player.garage) < car_index:
            raise IndexError("You don't have a car at given position")
        part_index = int(input('Enter the index of the part you want to repair: '))
        if player.garage[car_index].parts[car_index]:
            raise IndexError('Part is already repaired')
        mechanic_index = int(input('Choose one of mechanics with different chance to repair a part: '))
        print(player.repair(car_index, part_index, mechanics[mechanic_index]))
        player.move()
    case 4:
        player.move()
    case 5:
        for car in market.car_shelter:
            print(car)
    case 6: market.show_basic_info()
    case 7: print(player.garage)
    case 8:
        for client in clients:
            print(client)
    case 9: pass
    case 10: print(player.money)
    case 11: player.token = True
    case 12: pass
