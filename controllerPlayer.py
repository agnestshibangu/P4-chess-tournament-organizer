from MODELS.playersData import json_string
from MODELS.player import Player

import random
import json 

# ######################################

##### convertir fichier json en liste #####
data = json.loads(json_string)
players_list = data['players']
# ###########################################

def create_list_of_players(players_list):
    players = []
    i = 1
    for player in players_list:
            # player = Player('player_n°' + str(i), 0)
            player = Player(str(i), 0)
            players.append(player)
            print(player._number)
            i = i + 1
    return players




# def generate_pairs():
#     number_of_players = len(players_list)
#     number_of_pairs = round(number_of_players / 2)
#     tour = []

#     y = 1
#     for x in range(number_of_pairs):
#         matchName = str('Match' + str(y))
#         newMatch = []
#         newMatch.append(matchName)
#         for i in range(2):
#             choosen_player = random.choice(players_list)
#             newMatch.append(choosen_player)
#             players_list.remove(choosen_player)
#             i = i + 1
#         tour.append(newMatch)
#         print(newMatch)
#         y = y + 1
#     print(' ')


