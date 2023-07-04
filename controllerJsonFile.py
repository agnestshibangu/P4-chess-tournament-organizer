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
        
        
    print(dictionary)
 

#     # open json file
    with open('dataTournament.json') as json_file:
        data = json.load(json_file)
        print(data)

    
    print("Type:", type(data))
    print("tournament:", data['tournament'])


#     # Serializing json
    data['tournament'].append(dictionary)
    print(data)

#    # Writing to sample.json
    filename = 'dataTournament.json'
    with open(filename, 'w') as json_file:
        json.dump(data, json_file,
                                indent=4,
                                separators=(',',': '))
        


