from MODELS.player import Player


def create_list_of_players(players_list):
    players = []
    i = 1
    score = 0
    for player in players_list:
        player = Player('player_n°' + str(i), score, matches_history=[])
        players.append(player)
        i = i + 1
    return players