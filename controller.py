
from MODELS.tournament import Tournament 
from MODELS.tour import Tour
from MODELS.match import Match
import controllerTournament
import controllerTour

import sys


# --- creer un nouveau tournois  : TOURNOI
#     --- la création du tounois engendre x tours en fonction du nombre de participants TOUR
#         --- chaque tour créer x matchs MATCH 
#             --- chaque match retourne un resultat
#     --- on redistribue le nombre de joueurs restants en fonction des resultats 




def start_tournament():
    while True:         
        print("Voulez-vous démarrer un tournoi ? [Y/N]")    
        data = input()   
        if data == 'Y':
            print('starting a new tournament...')
            nb_of_players = controllerTournament.number_of_player()
            break
        elif data == 'N':
            print('good bye !')
            sys.exit()
        else:
            print('invalide answer')
    # créer un objet tournoi 
    create_a_tournament(nb_of_players)

def create_a_tournament(nb_of_players):
    newTournament = Tournament("Tournament", nb_of_players)
    nb_of_players = newTournament.number_of_players
    tours =  controllerTour.create_list_of_tours(nb_of_players)
    for tour in tours:
        i = 1
        while i < tour._number_of_matchs:
            
    


    # newMatch = Match("nouveau match")



start_tournament()


























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


