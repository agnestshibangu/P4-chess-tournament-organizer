from MODELS.match import Match
from VIEW.view import View
import random


def choose_two_players_first_tour(players):
    ''' This function create an array --> two_players_array = [], choose two random
    players from the list in parameter players. It removes the choosen player from the list
    and append it to the array. the variable y is initialized to 1 and when it reaches 2,
    the function stops.
    '''

    two_players_array = []
    y = 1
    for y in range(2):
        choosen_player = random.choice(players)
        players.remove(choosen_player)
        if y == 0:
            two_players_array.append(choosen_player)
        elif y == 1:
            two_players_array.append(choosen_player)
        y = y + 1
    return two_players_array


# choose two players and create a tuple
def choose_two_players_other_tours(players):
    ''' This function create an array --> two_players_array = [], choose qnd removes
    a random player from the list in parameter players and append it to the two_players_array.
    it then verifies that the second choosen player is different from the player's number that is sotred
    in the first player's history with while second_player == first_player.player_matches_history[0].
    if the two values are matching it means that this pair has already been created. so another player
    is choosen from the list if they are still multiple players in the list.
    '''
    two_players_array = []
    first_player = random.choice(players)
    players.remove(first_player)
    two_players_array.append(first_player)
    second_player = random.choice(players)
    while second_player == first_player.player_matches_history[0]:
        if len(players) > 1:
            View.message_player_same_as_history()
            second_player = random.choice(players)
    else:
        players.remove(second_player)
        two_players_array.append(second_player)
    return two_players_array


# add to history
def add_to_history(array):
    ''' For each players in the array that contains two players, the second player
    is appended to the player_matches_history array of the first player and vice versa.
    This ensures that the encounter is recorded when it will be time to generate pairs
    for the next tour and avoid identical encounters.
    '''
    for player in array:
        if player == array[0]:
            player.player_matches_history.clear()
            player.player_matches_history.append(array[1])
        if player == array[1]:
            player.player_matches_history.clear()
            player.player_matches_history.append(array[0])


# genere les matchs pour un tour
def generate_pairs_for_first_tour(players):
    ''' This function calls the function choose_two_player_first_tour() which takes as a parameter
    the list of players. It chooses two random players and save them in an array. Then the function
    add to history is called. finally, a object match is created with the array passed as an attribute
    and a method from the view is called to print the infos for each match.
    '''
    number_of_players = len(players)
    number_of_pairs = round(number_of_players / 2)
    tour = []
    i = 1
    for x in range(number_of_pairs):
        array = choose_two_players_first_tour(players)
        # add a player to the other player story
        add_to_history(array)
        match = Match('MATCH_' + str(i), array)
        tour.append(match)
        i = i + 1
    # DISPLAY INFOS ON THE MATCH
    View.print_infos_for_each_match(tour)
    return tour


def generate_pairs_for_a_tour(players):
    ''' This function calls the function choose_two_player_other_tour() which takes as a parameter
    the list of remaining players. It calls the function add_to_history for each player of the array
    parameter. It then append the new match to the array tour = []. Then the view method print the infos
    for each match.
    '''

    number_of_players = len(players)
    number_of_pairs = round(number_of_players / 2)
    tour = []
    i = 1
    for x in range(number_of_pairs):
        array = choose_two_players_other_tours(players)
        add_to_history(array)
        match = Match('MATCH_N°' + str(i), array)
        tour.append(match)
        i = i + 1
    View.print_infos_for_each_match(tour)
    return tour
