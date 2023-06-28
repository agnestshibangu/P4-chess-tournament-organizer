from MODELS.tournament import Tournament
from MODELS.tour import Tour
from MODELS.match import Match
import controllerTournament
import controllerTour
import controllerMatch
import controllerPlayer
import controllerRapport
from colorama import Fore, Back, Style
from VIEW.view import view


from MODELS.playersData import json_string
from MODELS.player import Player
import sys
import json

# ######################################

##### convertir fichier json en liste #####
data = json.loads(json_string)
players_list = data['players']

# ###########################################

# --- creer un nouveau tournois  : TOURNOI
#     --- la création du tounois engendre x tours en fonction du nombre de participants TOUR
#         --- chaque tour créer x matchs MATCH
#             --- chaque match retourne un resultat
#     --- on redistribue le nombre de joueurs restants en fonction des resultats

# generate JSON file
json_list_player_alpha = controllerRapport.sort_alpha_players(players_list)
print(json_list_player_alpha)
controllerRapport.convert_to_json(json_list_player_alpha)


def create_a_tournament():
    players = controllerPlayer.create_list_of_players(players_list)
    view.display_all_players(players)
    nb_of_players = len(players)
    newTournament = Tournament("tournament", nb_of_players)
    nb_of_players = newTournament.tournament_number_of_players
    newTournament.tournament_name
    # # créé un certain nombre de tours en fonction du nombre de participants
    tours =  controllerTour.create_list_of_tours(nb_of_players)
    while nb_of_players > 1:
        if newTournament.tournament_number_of_players == 1:
            view.print_final_winner(players)
        for tour in tours:
        #     # créé x matchs par tour
            if tour._name == 'TOUR N°1':
                view.print_first_tour_name(tour)
                tour_list_matches = controllerMatch.generate_pairs_for_first_tour(players)
                for match in tour_list_matches :
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
                print('---------------------------')
                print(str(tour._name) + 'EST TERMINE')



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


