from MODELS.player import Player


def create_list_of_players(players_list):
    ''' This function takes as a parameter the players_list, and retrieve for each players
    the data from the list to pass it to the player object as attributes and append the new
    player object that has been create to the list players.
    '''
    players = []
    i = 0
    for player in players_list:
        player_number = players_list[i]['number']
        player_family_name = players_list[i]['familyName']
        player_first_name = players_list[i]['firstName']
        player_birth_date = players_list[i]['birthDate']
        player_national_identifier = players_list[i]['nationalIdentifier']
        score = 0
        # # number, score, firstname, matcheshistory, birthdate, nationalidentifier
        # player = Player('player_°' + str(player_number),  player_family_name, player_first_name,
        player = Player(str(player_number),  player_family_name, player_first_name,
                        player_birth_date, player_national_identifier, score, matches_history=[])
        players.append(player)
        i = i + 1
    print(players)
    return players
