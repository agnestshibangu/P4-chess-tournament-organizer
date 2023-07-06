from MODELS.match import Match
from MODELS.player import Player
from VIEW.view import View
import random

# pour le premier tour, on peut choisir les joueurs au hasard

# pour les tours suivants on classe les joueurs :
#   * en fonction du nombre de points
#   * associer les joueurs dans l'ordre
#   * si plus de 2 joueurs ont le meme score, on les associent au hasard
#   * éviter les matchs identiques


# choose two players and create a tuple
def choose_two_players_first_tour(players):
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
    for player in array:
        if player == array[0]:
            player.player_matches_history.clear()
            player.player_matches_history.append(array[1])
        if player == array[1]:
            player.player_matches_history.clear()
            player.player_matches_history.append(array[0])


# genere les matchs pour un tour
def generate_pairs_for_first_tour(players):
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
