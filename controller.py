from MODELS.tournament import Tournament
import controllerTour as controllerTour
import controllerMatch as controllerMatch
import controllerPlayer as controllerPlayer
import controllerRapport as controllerRapport
import controllerJsonFile as controllerJsonFile 
from VIEW.view import view
import json

# CONTROLLER POUR LES RAPPORTS 

# generate brut text for list players of tournament by alpha order
# list_player_alpha = controllerRapport.sort_alpha_players(players_tournament_list)
# controllerRapport.convert_to_text_tournament_players(list_player_alpha)
# view.message_text_all_players()

#  generate brut text for all players by alpha order
# list_player_alpha_all = controllerRapport.sort_alpha_players(all_players_list)
# controllerRapport.convert_to_text_all_players(list_player_alpha_all)
# view.message_text_tournament_players()

# convertir fichier json en liste : liste de tout les joueurs #
with open('dataTournamentPlayers.json') as json_file:
    data = json.load(json_file)
    all_players_list = data['players']
    players_list = data['players']
# players list for the main controller
# infos for all tournaments
controllerRapport.text_file_for_all_tournament()
view.message_text_all_tournament_infos()

def create_a_tournament():
    # infos for single tournament
    controllerRapport.text_file_for_tournament()
    view.message_text_tournament_infos()
    players = controllerPlayer.create_list_of_players(players_list)
    view.display_all_players(players)
    nb_of_players = len(players)
    newTournament = Tournament("tournament", nb_of_players)
    nb_of_players = newTournament.tournament_number_of_players
    
    tours = controllerTour.create_list_of_tours(nb_of_players)

    for tour in tours:
        if tour._name == 'TOUR N_1' :
            view.print_first_tour_name(tour)
            controllerRapport.add_tour_to_tournament_infos(tour)
            #append tour to JSON file
            tour_list_matches = controllerMatch.generate_pairs_for_first_tour(players)
        else:
            controllerRapport.add_tour_to_tournament_infos(tour)
            #append tour to JSON file
           
            #append tour to JSON file
            tour_list_matches = controllerMatch.generate_pairs_for_a_tour(selected_players)        
        for match in tour_list_matches:
            tour._array_of_matches.append(match)
        print('JE SUIS LA WESH')
        print(tour._name)
        for match in tour._array_of_matches:
            print(match._name)
        controllerJsonFile.add_tour_to_tournament_json(tour)
        view.display_points_retreive_first_tour_start()
        first_tour_selected_players = controllerTour.get_tour_scores(tour_list_matches)
        for match in tour_list_matches:
            controllerRapport.add_matchs_tournament_infos(match)
        controllerRapport.add_end_time_tour_tournament_infos()
        selected_players = first_tour_selected_players
        newTournament.tournament_number_of_players = len(selected_players)
        if len(selected_players) == 1:
            winner = str(selected_players[0].player_number)
            controllerRapport.add_end_time_tournament_infos()
            controllerRapport.add_winner_tournament_infos(winner)
            print('LE GAGNANT EST :'+str(selected_players))
            print("LE GAGNANT EST : player's number :"+str(selected_players[0].player_number))


# controllerTournament.start_tournament()
def start():
    view.prompt_start_tournament()
start()

create_a_tournament()
