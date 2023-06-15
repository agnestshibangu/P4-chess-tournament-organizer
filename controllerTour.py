from MODELS.tour import Tour

def create_list_of_tours(nb_players):
    tours = []
    i = 1
    while nb_players != 1:
        number_of_matchs = round(nb_players/ 2)
        array = []
        tour = Tour('tour_n°' + str(i), number_of_matchs, array)
        print(tour._name)
        print(tour._number_of_matchs)  
        print(tour._array_of_matches)
        print(tour)
        tours.append(tour)
        nb_players = round(nb_players / 2)
        i = i + 1
    # print('since there are ' + str(initial_number_of_players) + ' players, ' + str(len(tours)) + ' rounds have been created')
    return tours


def retreive_single_score(player):
    print(player._number)
    print("entrez le score de ce joueur [WIN/LOO/TIE]")    
    result = input()   
    if result == 'w':
        print('CE JOUEUR A GAGNE LA PARTIE !')
        player.player_score += 1
        player.player_score
        print(' ')
    # if result == 'TIE':
    #     print('PARTIE NULLE')
    #     player[0].player_score += 0.5
    #     player[0].player_score
    #     print(' ')
    if result == 'l':
        print('CE JOUEUR A PERDU')
        player.player_score
        print(' ')
    return player

# cette fonction itère sur les matchs du premier tour, récupère les scores de chaque joueurs et créé un tableau des joueurs séléctionnés
def get_first_tour_scores(first_tour_list_matches):
    # tableau des joueurs gagnants du premier tour
    first_tour_array_selected = []
    for match in first_tour_list_matches:
        print('----------')
        print(match._name)
        for player in match._array:
            retreive_single_score(player)
            if player._score == 1 :
                first_tour_array_selected.append(player)
    print(first_tour_array_selected)
    print("----- la récupération des points pour ce tour est terminée ----- ")
    return first_tour_array_selected