from MODELS.player import Player


def create_list_of_players(players_list):
    players = []
    i = 1
    for player in players_list:
        player = Player(str(i), 0, [])
        players.append(player)
        i = i + 1
    return players
