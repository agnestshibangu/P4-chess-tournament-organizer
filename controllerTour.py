from MODELS.tour import Tour

def create_list_of_tours(nb_players):
    tours = []
    initial_number_of_players = nb_players
    number_of_players = nb_players
    i = 1
    while number_of_players != 1:
        number_of_matchs = round(number_of_players / 2)
        newTour = Tour('tour_n°' + str(i), number_of_matchs)
        print(newTour._name)
        print(number_of_matchs)  
        tours.append(newTour)
        number_of_players = round(number_of_players / 2)
        i = i + 1
      
    print('since there are ' + str(initial_number_of_players) + ' players, ' + str(len(tours)) + ' rounds have been created')
    print(tours)
    return tours

create_list_of_tours(16)
