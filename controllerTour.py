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
    # print(tours)
    return tours

# create_list_of_tours(16)