from MODELS.match import Match
from MODELS.player import Player
from MODELS.playersData import json_string
# from getkey import getkey, key

import random
import json

# ######################################
##### convertir fichier json en liste #####
data = json.loads(json_string)
players_list = data['players']
# ###########################################


##### fonction pour le test a retirer #####
def create_list_of_players(players_list):
    global players
    players = []
    i = 1
    score =  0
    for player in players_list:
            player = Player('player_n°' + str(i), score)
            players.append(player)
            player.player_number
            player.player_score
            i = i + 1
    return players
###########################################

# players = create_list_of_players(players_list)

# choose two players and create a tuple
def chooseTwoPlayers(players):
   # print('blabla')
    two_players_array = []
    player1 = []
    player2 = []
    y = 1
    for y in range(2):
        choosen_player = random.choice(players)
        # print('choosen player' + str(choosen_player))
        players.remove(choosen_player)
        if y == 0:
            two_players_array.append(choosen_player)
        elif y == 1:
            two_players_array.append(choosen_player)
        y = y + 1
    print(two_players_array)
    return two_players_array



# genere les matchs pour un tour
def generate_pairs_for_first_tour(players):
# def generate_pairs_for_first_tour(players):
    number_of_players = len(players)
    number_of_pairs = round(number_of_players / 2)
    tour = []
    i = 1
    for x in range(number_of_pairs):
        array = chooseTwoPlayers(players)
        match = Match('MATCH_N°' + str(i), array)
        tour.append(match)
        i = i + 1
    for match in tour:
        print(match._name)
        print(match._array)
    return tour


# on créé une fonction qui classe les joueurs et génère les paires pour les tours autre que le premier tour
def generate_pairs_for_tours(first_tour_selected_players):
    print(first_tour_selected_players)
     




