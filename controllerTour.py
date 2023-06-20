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
    if result == 't':
        print('PARTIE NULLE')
        player.player_score += 0.5
        player.player_score
        print(' ')
    if result == 'l':
        print('CE JOUEUR A PERDU')
        player.player_score
        print(' ')
    return player


#define the highest scores and append to the array of selected players selected = []
def largest(score_array):

    max = score_array[0].get('score')
    playyyyy = score_array[0]
    n = len(score_array)

    for i in range(1, n):
        if score_array[i].get('score') > max:
            max = score_array[i].get('score')
            playyyyy = score_array[i]
            

    return playyyyy





# cette fonction itère sur les matchs du premier tour, récupère les scores de chaque joueurs et créé un tableau des joueurs séléctionnés
def get_first_tour_scores(first_tour_list_matches):
    # tableau des joueurs gagnants du premier tour
    score_array = []
    selected = []
    # len_selected = len(selected)
    first_tour_array_selected = []
    # pour un martch de deux joueurs
    for match in first_tour_list_matches:
        print('----------')
        match_array_scores =  match._array
        print(match._name)
        # génère un tableau qui récuppère tout les scores pour pouvoir les trier et récupèrer les scores les plus élevés
        for player in  match_array_scores:
            retreive_single_score(player)
            dict = {'number' : player.player_number, 'score' : player.player_score }
            score_array.append(dict)
    print(score_array)
    print(score_array[0])
    while len(selected) < len(first_tour_list_matches):
        result = largest(score_array)
        print('i am the result')
        print(result)
        score_array.remove(result)
        selected.append(result)
    print(selected)







    # while len(selected) < len(first_tour_list_matches):
    #     largest(score_array, selected)
    # for score in selected:
    #     print(score)

















    #             if player._score == 0.5 :
    #                 first_tour_array_selected.append(player)
    #             if player._score == 0 :
    #                 first_tour_array_selected.append(player)
    #         print(first_tour_array_selected)
    # for player in first_tour_array_selected:
    #     player.player_score









    print("----- la récupération des points pour ce tour est terminée ----- ")
    return first_tour_array_selected