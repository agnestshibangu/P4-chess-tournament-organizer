from MODELS.tournament import Tournament
import CONTROLLERS.controllerTour as controllerTour
import CONTROLLERS.controllerMatch as controllerMatch
import CONTROLLERS.controllerPlayer as controllerPlayer
import CONTROLLERS.controllerRapport as controllerRapport
import CONTROLLERS.controllerJsonFile as controllerJsonFile
from VIEW.view import View
import json

# CONTROLLER POUR LES RAPPORTS

# generate brut text for list players of tournament by alpha order
# list_player_alpha = controllerRapport.sort_alpha_players(
#                     players_tournament_list)
# controllerRapport.convert_to_text_tournament_players(list_player_alpha)
# view.message_text_all_players()

#  generate brut text for all players by alpha order
# list_player_alpha_all = controllerRapport.sort_alpha_players(
#                         all_players_list)
# controllerRapport.convert_to_text_all_players(list_player_alpha_all)
# view.message_text_tournament_players()

# convertir fichier json en liste : liste de tout les joueurs #
with open('JSON/dataTournamentPlayers.json') as json_file:
    data = json.load(json_file)
    all_players_list = data['players']
    players_list = data['players']
# players list for the main controller
# infos for all tournaments
controllerRapport.text_file_for_all_tournament()
View.message_text_all_tournament_infos()


def create_a_tournament():

    ''' When a new tournament starts, a text file containing all of the infos of this tournament is added,
    then a player list is created based on the players stored un the JSON file dataTournamentPlayers.json.
    A new tournament is created, with the number of players as a parameter to calculate the number of tours
    and matches. Then a list of tours is created.
    '''
    controllerRapport.text_file_for_tournament()
    View.message_text_tournament_infos()
    players = controllerPlayer.create_list_of_players(players_list)
    View.display_all_players(players)
    nb_of_players = len(players)
    newTournament = Tournament("tournament", nb_of_players)
    nb_of_players = newTournament.tournament_number_of_players
    tours = controllerTour.create_list_of_tours(nb_of_players)
    ''' for the first tour, the controllerRapport allows to add infos on the tour to the tournament
    infos text file. Then from the controller Match, random pairs are generated with the
    generate_pairs_for_first_tour() function that takes as a parameter the list of players.
    '''
    for tour in tours:
        if tour._name == 'TOUR N_1':
            View.print_first_tour_name(tour)
            controllerRapport.add_tour_to_tournament_infos(tour)
            # append tour to JSON file
            tour_list_matches = controllerMatch.generate_pairs_for_first_tour(
                                players)
        else:
            ''' for the other tours, pairs are generated based on the player's history, if they
            have already played against the player that is stored in their array history, the program
            will select another player for the new tour.
            '''
            controllerRapport.add_tour_to_tournament_infos(tour)
            tour_list_matches = controllerMatch.generate_pairs_for_a_tour(
                                selected_players)

            ''' for every matches of the tour, the new match is append to the array tour._array_of_matches
            Then the infos of the tour are appended to the json file. Then based on the return of the function
            get_tour_scores(tour_list_matches), an array of the sleected players is created.
            '''

        for match in tour_list_matches:
            tour._array_of_matches.append(match)
        controllerJsonFile.add_tour_to_tournament_json(tour)
        View.display_points_retreive_first_tour_start()
        first_tour_selected_players = controllerTour.get_tour_scores(
                                      tour_list_matches)
        # retreive data in json for a tour
        # controllerJsonFile.add_tour_to_tournament_json(tour)
        ''' for each match, the data is added to the text report, the end time is added.
        An other tour is generated until the number of selected players is equal to one.
        In the case a function to display the winner in the view is called and the data
        of the end of tournament is added to the text and json file.
        '''
        for match in tour_list_matches:
            controllerRapport.add_matchs_tournament_infos(match)
        controllerRapport.add_end_time_tour_tournament_infos()
        selected_players = first_tour_selected_players
        newTournament.tournament_number_of_players = len(selected_players)
        if len(selected_players) == 1:
            winner = str(selected_players[0].player_number)
            controllerRapport.add_end_time_tournament_infos()
            controllerRapport.add_winner_tournament_infos(winner)
            View.print_winner(selected_players)


# controllerTournament.start_tournament()
def start():
    View.prompt_start_tournament()


start()

create_a_tournament()
