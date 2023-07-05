import json

def add_tour_to_tournament_json(tour):

    tour_matchs = []

    dictionary = {
        "tour": tour._name,
        "tour_matches": tour_matchs,
    }

    for match in tour._array_of_matches:
        matchArray = []
       
        for player in match._array:
            playerArray = []
            playerArray.append("player number " + player._number)
            playerArray.append("player score " + str(player._score))
            matchArray.append(playerArray)

        dict = {
            "matchName" :  match._name,
            "players" : matchArray

        }
        dictionary["tour_matches"].append(dict)
    
#     # open json file
    with open('JSON/dataTournament.json') as json_file:
        data = json.load(json_file)

#     # Serializing json
    data['tournament'].append(dictionary)

#    # Writing to sample.json
    filename = 'JSON/dataTournament.json'
    with open(filename, 'w') as json_file:
        json.dump(data, json_file,
                                indent=4,
                                separators=(',',': '))
        


