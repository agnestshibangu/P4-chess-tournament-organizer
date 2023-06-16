
from MODELS.tournament import Tournament 
from MODELS.tour import Tour
from MODELS.match import Match
import controllerTournament
import controllerTour
import controllerMatch
import controllerPlayer

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
#     --- on redistribue le nombre de joueurs restants en fonction des resultats \

def create_a_tournament():
    players = controllerPlayer.create_list_of_players(players_list)
    nb_of_players = len(players)
    newTournament = Tournament("Tournament", nb_of_players)
    nb_of_players = newTournament.number_of_players
    # # créé un certain nombre de tours en fonction du nombre de participants
    tours =  controllerTour.create_list_of_tours(nb_of_players)
    print(' ')
    print(tours)
    for tour in tours:
    #     # créé x matchs par tour
        if tour._name == 'tour_n°1':
            print('c est le premier tour donc on melange les joueurs au hasard')
            first_tour_list_matches = controllerMatch.generate_pairs_for_first_tour(players)
            for match in first_tour_list_matches :
                tour._array_of_matches.append(match)
            print(tour._array_of_matches)
            # on récupère les vainqueurs du premier match
            first_tour_selected_players = controllerTour.get_first_tour_scores(first_tour_list_matches)
            # print('je suis dans le controller, voici la liste des gagnants du premier tour') 
            # print(first_tour_selected_players)
        else : 
            # controllerMatch.retreive_scores_for_each_match(tour)
            print('hello')
            print(tour._name)
            controllerMatch.generate_pairs_for_tours(first_tour_selected_players)

controllerTournament.start_tournament()
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


