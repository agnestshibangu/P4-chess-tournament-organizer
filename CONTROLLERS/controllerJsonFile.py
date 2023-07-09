import json


def add_tour_to_tournament_json(tour):
    ''' This function takes as a parameter the object tour, creates a dictionary and append
    to it the name and an empty array that will contain the number of matches for this tour
    and append to it all of the matches that are stored in his attribute .array_of_matches
    with their own attributes concerning each players (player._number and player._score) 
    it returns a dictionary that contains the informations of each match.
    It then opens the json file that contains the data of the current tournament
    and append the data to the already existing data data['tournament'] and then save
    the entire new dicitonary.   
    '''
    
    tour_matchs = []
    dictionary = {
        "tour": tour._name,
        "tour_matches": tour_matchs,
    }

    for match in tour._array_of_matches:
        matchArray = []
        for player in match._array:
            playerArray = []
            playerArray.append({"player number " : player._number})
            playerArray.append({"player score " : str(player._score)})
            matchArray.append(playerArray)

        match_dict = {
            "matchName": match._name,
            "players": matchArray
        }
        dictionary["tour_matches"].append(match_dict)
    # open json file
    with open('JSON/dataTournament.json') as json_file:
        data = json.load(json_file)

    # Serializing json
    data['tournament'].append(dictionary)

    # Writing to sample.json
    filename = 'JSON/dataTournament.json'
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4, separators=(',', ': '))


def get_player_score_from_json():
    score = 1
    with open('../JSON/dataTournament.json') as json_file:
        data = json.load(json_file)
    for i in data['tournament']:
        for i in i['tour_matches']:
            print(i["matchName"])
            for i in i['players']:
                print(i[1])
                i[1]["player score "] = score 
                print(i[1])
            
             
def get_single_player_dict_for_json(player_dict):
    print(player_dict)

