import os
from datetime import datetime
from pathlib import Path


# PLAYERS infos report TEXT FORMAT
def sort_alpha_players(players_list):
    def return_first_name(player):
        return player['firstName']
    players_list.sort(key=return_first_name)
    sorted_list = players_list
    return sorted_list


def convert_to_text_all_players(sorted_list):
    directory = "REPORT"
    if not os.path.exists(directory):
        os.makedirs(directory)

    path = 'REPORT/all-player.txt'

    with open(path, 'w') as f:
        f.write('_____________________________________________________')
        f.write('\n')
        f.write('|                                                    |')
        f.write('\n')
        f.write('|    ALL PLAYERS LIST (by alphabetical order)        |')
        f.write('\n')
        f.write('|                                                    |')
        f.write('\n')
        f.write('______________________________________________________')
        f.write('\n')
        for line in sorted_list:
            f.write('\n')
            f.write(str(line).replace("{", "").replace("}", ""))
            f.write('\n')


def convert_to_text_tournament_players(sorted_list):
    directory = "REPORT"
    if not os.path.exists(directory):
        os.makedirs(directory)

    path = 'REPORT/tournament-player.txt'

    with open(path, 'w') as f:
        f.write('______________________________________________________')
        f.write('\n')
        f.write('|                                                     |')
        f.write('\n')
        f.write('|   TOURNAMENT PLAYERS LIST (by alphabetical order)   |')
        f.write('\n')
        f.write('|                                                     |')
        f.write('\n')
        f.write('_____________________________________________________')
        f.write('\n')
        for line in sorted_list:
            f.write('\n')
            f.write(str(line).replace("{", "").replace("}", ""))
            f.write('\n')

# TOURNAMENT infos report JSON FORMAT
def text_file_for_tournament():
    def Horodatage():
        x = datetime.now()
        year = str(x.year)
        month = str(x.month)
        day = str(x.day)
        currentDate = year + '-' + month + '-' + day
        return str(currentDate)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    Horodatage()
    date = Horodatage()

    directory = "REPORT"
    if not os.path.exists(directory):
        os.makedirs(directory)

    path = 'REPORT/new-tournament-infos.txt'

    tournament_title = input("Entrez un nom pour le tournoi: ")

    with open(path, 'w') as f:
        f.write('_______________________________________________________')
        f.write('\n')
        f.write('|                                                      |')
        f.write('\n')
        f.write('|                  NEW TOURNAMENT INFOS                |')
        f.write('\n')
        f.write('|                                                      |')
        f.write('\n')
        f.write('_______________________________________________________')
        f.write('\n')
        f.write('\n')
        f.write(' this is the tournament title : ' + tournament_title)
        f.write('\n')
        f.write(' this is the date of the tournament : ' + date)
        f.write('\n')
        f.write(' this is the start time of the tournament : ' + current_time)

    path_all_tournaments = 'REPORT/all-tournaments.txt'

    with open(path_all_tournaments, 'a') as f:
        f.write('_______________________________________________________')
        f.write('\n')
        f.write(' this is the tournament title : ' + tournament_title)
        f.write('\n')
        f.write(' this is the date of the tournament : ' + date)
        f.write('\n')
        f.write(' this is the start time of the tournament : ' + current_time)
        f.write('\n')


# ALL TOURNAMENT infos report TEXT FORMAT
def text_file_for_all_tournament():

    path = Path('REPORT/all-tournaments.txt')
    if path.is_file():
        return "exists"
    else:
        with open(path, 'w') as f:
            f.write('___________________________________________')
            f.write('\n')
            f.write('|                                         |')
            f.write('\n')
            f.write('|           ALL TOURNAMENTS LIST          |')
            f.write('\n')
            f.write('|                                         |')
            f.write('\n')
            f.write('___________________________________________')
            f.write('\n')


def add_end_time_tournament_infos():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    path_all_tournaments = 'REPORT/all-tournaments.txt'
    with open(path_all_tournaments, 'a') as f:
        f.write(' this is the end of the tournament : ' + current_time)
        f.write('\n')


def add_winner_tournament_infos(winner):
    path_all_tournaments = 'REPORT/all-tournaments.txt'
    with open(path_all_tournaments, 'a') as f:
        f.write(' winner of the tournament : player num ' + winner)
        f.write('\n')
        f.write('___________________________________________________________')


def add_tour_to_tournament_infos(tour):
    tour_name = tour._name
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    path_new_tournaments = 'REPORT/new-tournament-infos.txt'
    with open(path_new_tournaments, 'a') as f:
        f.write('\n')
        f.write('\n')
        f.write(tour_name)
        f.write('\n')
        f.write('           this is the start time of the tour : ' +
                current_time)
        f.write('\n')


def add_matchs_tournament_infos(match):

    match_name = match._name

    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")

    path_new_tournaments = 'REPORT/new-tournament-infos.txt'
    with open(path_new_tournaments, 'a') as f:
        f.write('\n')
        f.write('\n')
        f.write('           ' + match_name)
        for player in match._array:
            f.write('\n')
            f.write('\n')
            f.write('           ' + 'player number : ' + player.player_number +
                    '           ' + 'player score |'
                    + str(player.player_score) + '|')
        f.write('\n')
        f.write('\n')


def add_end_time_tour_tournament_infos():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    path_new_tournaments = 'REPORT/new-tournament-infos.txt'
    with open(path_new_tournaments, 'a') as f:
        f.write('\n')
        f.write('           this is the end time of the tour : ' +
                current_time)
        f.write('\n')
