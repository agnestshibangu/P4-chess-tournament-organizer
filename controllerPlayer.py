from MODELS.playersData import json_string
from MODELS.player import Player

import random
import json 

# ######################################

##### convertir fichier json en liste #####
data = json.loads(json_string)
players_list = data['players']
# ###########################################


#_________________________________________________________________________________________________#

def create_list_of_players(players_list):
    players = []
    i = 1
    for player in players_list:
            # player = Player('player_n°' + str(i), 0)
            player = Player(str(i), 0, [])
            players.append(player)
            print(player._number)
            i = i + 1
    return players


#_________________________________________________________________________________________________#
