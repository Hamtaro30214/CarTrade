import random

from Client import Client
from Player import Player


player = Player()
print(player.money)
player.generate_car()
player.generate_car()
player.money = 900
print(player.garage)
print(player.money)
player.start_game(player)
# TODO: separate function to generate new cars
for _ in range(random.randint(5, 10)):
    player.generate_car()
print(len(player.garage), player.garage)
client1 = Client()
clients = []
for _ in range(3):
    clients.append(Client())
for client in clients:
    print(client)
