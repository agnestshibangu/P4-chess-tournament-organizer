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
    players = []
    i = 1
    for player in players_list:
            player = Player('player_n°' + str(i))
            players.append(player)
            print(player)
            i = i + 1
    return players
###########################################

players = create_list_of_players(players_list)

# choose two players and create a tuple
def chooseTwoPlayers(players):
    two_players_array = []
    player1 = []
    player2 = []
    player1Score = []
    player2Score = []
    y = 1
    for y in range(2):
        # print('y value : ' + str(y))
        # on itere sur le tableau player donc on est sensé avoir un player en tant qu'objet
        choosen_player = random.choice(players)
        print(choosen_player)
        players.remove(choosen_player)
        if y == 0:
            player1.append(choosen_player)
            player1.append(player1Score)
            two_players_array.append(player1)
        elif y == 1:
            player2.append(choosen_player)
            player2.append(player2Score)
            two_players_array.append(player2)
        y = y + 1
    # print('two player array')
    # print(two_players_array)
    return two_players_array
    # print(' ')

# genere les matchs pour un tour 
def generate_pairs_for_first_tour(players):
# def generate_pairs_for_first_tour(players):
    number_of_players = len(players_list)
    number_of_pairs = round(number_of_players / 2)
    tour = []
    y = 1
    i = 1 
    for x in range(number_of_pairs): 
        array = chooseTwoPlayers(players_list)
        match = Match('match_n°' + str(i), array)
        tour.append(match)
        i = i + 1
    print(tour)
    for match in tour:
        print(match._name)
        print(match._array)


first_tour_list_matches = generate_pairs_for_first_tour(players)

def retreive_score(first_tour_list_matches):









    

# def retreive_scores_for_each_match(tour):
#     nextTourWinners = []
#     for match in tour:
#         print(' ')
#         print(match._name)
#         print(match._array)
#         player1 = match._array[0]
#         player2 = match._array[1]
#         print(' ')
#         print('qui a gagné ce match ? ')
#         data = input()   
#         if data == '1':
#             nextTourWinners.append(player1)
#             print('player 1 participera au prochain tour ! ')
#         elif data == '2':
#             nextTourWinners.append(player2)
#             print('player 2 participera au prochain tour ! ')
#         else:
#             print('invalide answer')
#     print(nextTourWinners)


# tour = generate_pairs_for_first_tour(players_list)
# for match in tour:
#     print(match._array)

# tour = generate_pairs(players_list)

# retreive_scores_for_each_match(tour)




# print("press enter")
# var = getkey()

# if var == key.ENTER:
#   print("You pressed enter")
# else:
#   print("You didnt")