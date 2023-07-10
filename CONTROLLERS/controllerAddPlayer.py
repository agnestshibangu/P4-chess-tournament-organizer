import json


def add_a_new_player():
    '''This function retreive some input from the user with the terminal (id, firstname)
    open the json file, creates a dictionary --> player_dict that contains the player's data,
    append it to the existing data[players] dictionary and save the updated dicitonary
    in the json file.
    '''
    # get new player data
    new_player_id = input("Entrez l'id du joueur: ")
    new_player_firstName = input("Entrez le prénom du joueur: ")

    with open('dataTournamentPlayers.json') as json_file:
        data = json.load(json_file)
    player_dict = {
        "id": new_player_id,
        "firstName": new_player_firstName
    }
    data['players'].append(player_dict)
    filename = 'dataTournamentPlayers.json'
    with open(filename, 'w') as json_file:
        json.dump(data, json_file,
                  indent=4,
                  separators=(',', ': '))
