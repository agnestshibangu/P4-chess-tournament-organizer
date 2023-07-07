from MODELS.tour import Tour
from VIEW.view import View
from datetime import datetime


def create_list_of_tours(nb_players):
  
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
        # array = []
        tour = Tour('TOUR N_' + str(i), date, number_of_matches, array_of_matches,
                    start_time, end_time)
        # tour = Tour('TOUR N_' + str(i), number_of_matches, array)
        tours.append(tour)
        nb_players = round(nb_players / 2)
        i = i + 1
    return tours


def retreive_single_score(player):
    View.retreive_single_score_view(player)
    # return player


# players_list[0].player_number define the highest scores and append to the
# array of selected players selected = []
def largest(score_array):
    max_score = score_array[0].get('score')
    selected_player = score_array[0]
    n = len(score_array)
    for i in range(1, n):
        if score_array[i].get('score') > max_score:
            max_score = score_array[i].get('score')
            selected_player = score_array[i]
    return selected_player


def sort_players_list_object(tour_array_selected, copy_list_player):
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
    # tableau des joueurs gagnants du premier tour
    score_array = []
    tour_array_selected = []
    copy_list_player = []
    # pour un martch de deux joueurs
    for match in tour_list_matches:
        View.print_separator()
        match_array_scores = match._array
        # génère un tableau qui récuppère tout les scores pour pouvoir
        # les trier et récupèrer les scores les plus élevés
        for player in match_array_scores:
            View.retreive_single_score(player)
            # créer une copie de la liste player
            copy_list_player.append(player)
            dict = {'number': player.player_number,
                    'score': player.player_score}
            score_array.append(dict)
    while len(tour_array_selected) < len(tour_list_matches):
        result = largest(score_array)
        score_array.remove(result)
        tour_array_selected.append(result)
    array_selected = sort_players_list_object(tour_array_selected,
                                              copy_list_player)
    View.display_points_retreive_first_tour_end()
    return array_selected
