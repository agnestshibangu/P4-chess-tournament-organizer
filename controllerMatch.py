from MODELS.match import Match
from MODELS.playersData import json_string
# from getkey import getkey, key

import random
import json 

# ######################################
##### convertir fichier json en liste #####
data = json.loads(json_string)
players_list = data['players']
# ###########################################

def chooseTwoPlayers(players_list):
    y = 1
    players_arra = []
    for i in range(2):
        choosen_player = random.choice(players_list)
        players_list.remove(choosen_player)
        y = y + 1
        players_arra.append(choosen_player)
    return players_arra

# genere les matchs pour un tour 
def generate_pairs(players_list):
    number_of_players = len(players_list)
    number_of_pairs = round(number_of_players / 2)
    tour = []
    y = 1
    i = 1 
    for x in range(number_of_pairs): 
        arra = chooseTwoPlayers(players_list)
        match = Match('match_n°' + str(i), arra)
        tour.append(match)
        i = i + 1
    print(tour)
    return tour
    for match in tour:
        print(match._name)
        print(match._array)


def retreive_scores_for_each_match(tour):
    nextTourWinners = []
    for match in tour:
        print(' ')
        print(match._name)
        print(match._array)
        player1 = match._array[0]
        player2 = match._array[1]
        print(' ')
        print('qui a gagné ce match ? ')
        data = input()   
        if data == '1':
            nextTourWinners.append(player1)
            print('player 1 participera au prochain tour ! ')
        elif data == '2':
            nextTourWinners.append(player2)
            print('player 2 participera au prochain tour ! ')
        else:
            print('invalide answer')
    print(nextTourWinners)

# tour = generate_pairs(players_list)

# retreive_scores_for_each_match(tour)




# print("press enter")
# var = getkey()

# if var == key.ENTER:
#   print("You pressed enter")
# else:
#   print("You didnt")