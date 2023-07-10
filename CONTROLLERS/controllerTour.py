from MODELS.tour import Tour
from VIEW.view import View
from datetime import datetime
import CONTROLLERS.controllerJsonFile as controllerJsonFile


def create_list_of_tours(nb_players):
    ''' this function creates a number of tours based on the number of players,
    it calculates the number of matches by dividing the number of players by 2
    until the number of players is equal to 1. each tour that is being added to the list
    of tours is being stored as an object from the MODELS named Tour and takes as an attribute
    a number, a date, a number of matches, a start time and an end time
    ('TOUR N_' + str(i), date, number_of_matches, array_of_matches, start_time, end_time)
    '''

    x = datetime.now()
    year = str(x.year)
    month = str(x.month)
    day = str(x.day)
    date = year + '-' + month + '-' + day

    tours = []
    i = 1
    start_time = "startime"
    end_time = "endtime"

    while nb_players != 1:
        number_of_matches = round(nb_players / 2)
        array_of_matches = []
        tour = Tour('TOUR N_' + str(i), date, number_of_matches, array_of_matches,
                    start_time, end_time)
        tours.append(tour)
        nb_players = round(nb_players / 2)
        i = i + 1
    return tours


def retreive_single_score(player):
    ''' this function simply calls the view method retreive_single_score_view(player) that takes as a parameter
    the list of players to ask to user an score input for each player'''
    View.retreive_single_score_view(player)


def largest(score_array):
    ''' This function has a max_score that is initialized at the first value of the array score_array[0].
    for i in range of n the length of the array, if the score of the current player is superior to the value
    max_score, the player who has that max score becomes the selected_player value and is being returned.
    '''
    max_score = score_array[0].get('score')
    selected_player = score_array[0]
    n = len(score_array)
    for i in range(1, n):
        if score_array[i].get('score') > max_score:
            max_score = score_array[i].get('score')
            selected_player = score_array[i]
    return selected_player


def sort_players_list_object(tour_array_selected, copy_list_player):
    ''' for i in range of 0 to the length of the array tour_array_selected, if a player in the array
    copy_list_player happens to have the same number as in the list tour_array_selected, it means that
    the player has been selected, so it is added to the array_select. The array_selected is being return
    and contains the data of the selected players.
    '''
    n = len(tour_array_selected)
    array_selected = []
    for player in copy_list_player:
        for i in range(0, n):
            if player.player_number == tour_array_selected[i].get('number'):
                array_selected.append(player)
    return array_selected


# cette fonction itère sur les matchs du premier tour, récupère les scores de
# chaque joueurs et créé un tableau des joueurs séléctionnés
def get_tour_scores(tour_list_matches):
    ''' This function creates 3 arrays score_array = [], tour_array_selected = [], copy_list_player = []
    for every matches in tour_list_matches, it retreives the array of the match --> match._array and for each
    player contained in the array, the function retreive_single_score(player) asks for the input of the user
    for each player and append the player to the array copy_list_player. Then it creates a dictionary called
    player_dict with the number and the score of the player, and pass it so it can be updated to the json file
    of the tournament with the function controllerJsonFile.get_player_score_from_json(player_dict). It is also
    append to the array --> score_array[]. while the length of the tour_array_selected is inferior to
    tour_list_matches, the highest score is retreive with the function largest(score_array) in the score_array.
    Then it is removed from the array and append to the tour_array_selected. Then it returns as a view that the
    retreiving of the points is over.
    '''

    # tableau des joueurs gagnants du premier tour
    score_array = []
    tour_array_selected = []
    copy_list_player = []
    # pour un martch de deux joueurs
    for match in tour_list_matches:
        View.print_separator()
        match_array_scores = match._array
        for player in match_array_scores:
            View.retreive_single_score(player)
            copy_list_player.append(player)
            player_dict = {'number': player.player_number,
                           'score': player.player_score}
            controllerJsonFile.get_player_score_from_json(player_dict)
            score_array.append(player_dict)
    while len(tour_array_selected) < len(tour_list_matches):
        result = largest(score_array)
        score_array.remove(result)
        tour_array_selected.append(result)
    array_selected = sort_players_list_object(tour_array_selected,
                                              copy_list_player)
    View.display_points_retreive_first_tour_end()
    return array_selected
