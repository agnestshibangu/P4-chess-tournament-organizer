import json

def add_a_new_player():
    #get new player data
    new_player_id = input("Entrez l'id du joueur: ")
    new_player_firstName = input("Entrez le prénom du joueur: ")

    player_dict = {}
    my_information = {"id": new_player_id, 
                      "firstName": new_player_firstName}

    with open('dataTournamentPlayers.json') as json_file:
        data = json.load(json_file)

        print("Type:", type(data))
        print("players:", data['players'])
      
    data['players'].append(my_information)
    filename = 'dataTournamentPlayers.json'
    with open(filename, 'w') as json_file:
        json.dump(data, json_file,
                                indent=4,
                                separators=(',',': '))
        
add_a_new_player()
    

