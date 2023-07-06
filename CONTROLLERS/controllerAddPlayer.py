import json


def add_a_new_player():
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
