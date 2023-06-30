from MODELS.tournament import Tournament
from MODELS.tour import Tour
from MODELS.match import Match
import controllerTournament as controllerTournament
import controllerTour as controllerTour
import controllerMatch as controllerMatch
import controllerPlayer as controllerPlayer
import controllerRapport as controllerRapport
from colorama import Fore, Back, Style
from VIEW.view import view
import os


# from JSON.playersTournamentData import json_string
from JSON.allPlayersData import json_string_all
from JSON.playersTournamentData import json_string
from MODELS.player import Player
import sys
import json

# ######################################
data = json.loads(json_string_all)

##### convertir fichier json en liste : liste des joueurs du tournoi #####
data = json.loads(json_string)
players_tournament_list = data['players']
players_list = data['players']

##### convertir fichier json en liste : liste de tout les joueurs #####
data = json.loads(json_string_all)
all_players_list = data['players']
# players list for the main controller

# ###########################################


################################################
####### CONTROLLER POUR LES RAPPORTS ###########
################################################

# # # generate brut text for list players of tournament by alpha order
# list_player_alpha = controllerRapport.sort_alpha_players(players_tournament_list)
# controllerRapport.convert_to_text_tournament_players(list_player_alpha)
# view.message_text_all_players()

# # # generate brut text for all players by alpha order
# list_player_alpha_all = controllerRapport.sort_alpha_players(all_players_list)
# controllerRapport.convert_to_text_all_players(list_player_alpha_all)
# view.message_text_tournament_players()

#infos for all tournaments
controllerRapport.text_file_for_all_tournament()
view.message_text_all_tournament_infos()




################################################
####### CONTROLLER POUR CREER UN TOURNOI #######
################################################


def create_a_tournament():

    #######
    # infos for single tournament
    controllerRapport.text_file_for_tournament()
    view.message_text_tournament_infos()
    # controllerRapport.append_text_for_all_tournament()
    #######

    players = controllerPlayer.create_list_of_players(players_list)
    view.display_all_players(players)
    nb_of_players = len(players)
    newTournament = Tournament("tournament", nb_of_players)
    nb_of_players = newTournament.tournament_number_of_players
    newTournament.tournament_name
    # # créé un certain nombre de tours en fonction du nombre de participants
    tours =  controllerTour.create_list_of_tours(nb_of_players)

    # if nb_of_players == 1:
    #     controllerRapport.add_end_time_tournament_infos()
    #     print(len(players))
    # while nb_of_players > 1:
       
    for tour in tours:
    #     # créé x matchs par tour
        tourName = tour._name
        # controllerRapport.add_tours_tournament_infos(tourName)
        if tour._name == 'TOUR N°1':
            view.print_first_tour_name(tour)
            controllerRapport.add_tours_tournament_infos(tour)
            tour_list_matches = controllerMatch.generate_pairs_for_first_tour(players)
            for match in tour_list_matches :
                matchName = match._name
                controllerRapport.add_matchs_tournament_infos(match)
                tour._array_of_matches.append(match)
                
            # print(tour._array_of_matches)
            # on récupère les selectionnés du premier match
            view.display_points_retreive_first_tour_start()
            first_tour_selected_players = controllerTour.get_tour_scores(tour_list_matches)
            # print(first_tour_selected_players)
            selected_players = first_tour_selected_players
            newTournament.tournament_number_of_players = len(selected_players)
            newTournament.tournament_number_of_players
            print('-------------------------')
            print('LA LISTE DES JOUEURS SELECTIONNES')
            for player in selected_players:
                print("player's number : " + str(player.player_number) + " --- SCORE : " + str(player._score))
            # TEST TO ADD END TIME TOURNAMENT TO ALL TOURNAMENTS INFOS FILE
            # controllerRapport.add_end_time_tournament_infos()
            print('-------------------------')
        else :
            tour._name
            tour_list_matches = controllerMatch.generate_pairs_for_a_tour(selected_players)
            for match in tour_list_matches :
                tour._array_of_matches.append(match)
            # print(tour._array_of_matches)
            # on récupère les selectionnés du premier match
            first_tour_selected_players = controllerTour.get_tour_scores(tour_list_matches)
            print(first_tour_selected_players)
            selected_players = first_tour_selected_players
            newTournament.tournament_number_of_players = len(selected_players)

            # display player
            if len(selected_players) == 1:
                winner = str(selected_players[0].player_number)
                controllerRapport.add_end_time_tournament_infos()
                controllerRapport.add_winner_tournament_infos()
                print ('LE GAGNANT EST : ' + str(selected_players) )        
                print ("LE GAGNANT EST : player's number :" + str(selected_players[0].player_number))     
               
            
            print('---------------------------')
            print(str(tour._name) + 'EST TERMINE')
    



################################################
##### CONTROLLER POUR AJOUTER DES JOUEURS ######
################################################

# controllerTournament.start_tournament()
def start():
    view.prompt_start_tournament()
start()

create_a_tournament()





























# tournament = Tournament("new tournament created")
# print(tournament.name)

# Tour.create_list_of_tours()

# Tour.display_current_round()

# Tour.generate_pairs()






#     def create_a_tour():
#         print('a new tour has been created')

#     def create_list_of_tours():
#         tours = []
#         initial_number_of_players = len(players_list)
#         number_of_players = len(players_list)
#         i = 1
#         while number_of_players != 1:
#             number_of_players = round(number_of_players / 2)
#             roundName = 'round' + str(i)
#             tours.append(roundName)
#             i = i + 1
#         print('since there are ' + str(initial_number_of_players) + ' players, ' + str(len(tours)) + ' rounds have been created')
#         print(' ')
#         print(tours)
#         print(' ')

#     def display_current_round():
#         print(' ')
#         print('current round : Round 1')
#         print(' ')


# ################################################################################################
# ########## On génère les paires à partir de la liste des players dans le fichier JSON ##########
# ################################################################################################

#     def generate_pairs():
#         number_of_players = len(players_list)
#         #print(number_of_players)

#         number_of_pairs = round(number_of_players / 2)
#         #print(number_of_pairs)

#         tour = []

#         y = 1
#         for x in range(number_of_pairs):
#             matchName = str('Match' + str(y))
#             newMatch = []
#             newMatch.append(matchName)
#             for i in range(2):
#                 choosen_player = random.choice(players_list)
#                 newMatch.append(choosen_player)
#                 players_list.remove(choosen_player)
#                 i = i + 1
#             tour.append(newMatch)
#             print(newMatch)
#             y = y + 1
#         print(' ')

#     def create_a_new_match():
#         print("a new match has been created")


# #### recuperer la date du jour ####
# ###################################
# ######## créer un dossier #########


# # def Horodatage():
# #     x = datetime.datetime.now()
# #     year = str(x.year)
# #     month = str(x.month)
# #     day = str(x.day)
# #     currentDate = year + '-' + month + '-' + day
# #     return str(currentDate)

# # Horodatage()
# # currentDate = Horodatage()

# # #####

# # folder = str('../Data/new-tournament/' + 'currentDate' + '/')
# # file = 'file.py'
# # print(folder)
# # if not os.path.exists(folder):
# #     os.makedirs(folder)
# # open('../Data/new-tournament/currentDate/myfile.py', "x")


