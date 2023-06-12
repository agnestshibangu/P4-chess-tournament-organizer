from MODELS.match import Match

def create_list_of_matchs(nb_matchs):
    matchs = []
    i = 1
    while i <= nb_matchs:
        match = Match('match_n°' + str(i))
        print(match._name)
        print(match)
        matchs.append(match)
        i = i + 1
        
    # print('since there are ' + str(initial_number_of_players) + ' players, ' + str(len(tours)) + ' rounds have been created')
    # print(tours)
    return matchs

create_list_of_matchs(16)