import json


def add_tour_to_tournament_json(tour):

    tourName = tour._name
    tourNumberMatches = tour._number_of_matchs 
    tourArrayMatches = tour._array_of_matches
   
    print(tourName)
    print(tourNumberMatches)

    print(tourArrayMatches)
    for match in tourArrayMatches:
        match._array
        for player in match._array:
            print(player._number)
            print(player._score)




    with open('dataTournament.json') as json_file:
        data = json.load(json_file)
        print(data)

    
    print("Type:", type(data))
    print("tournament:", data['tournament'])


    # Serializing json
    data['tournament'].append(tourName)
    print(data)

#    # Writing to sample.json
    filename = 'dataTournament.json'
    with open(filename, 'w') as json_file:
        json.dump(data, json_file,
                                indent=4,
                                separators=(',',': '))
        


