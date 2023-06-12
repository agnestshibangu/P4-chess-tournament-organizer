from MODELS.playersData import json_string

import json
# ######################################

# ##### convertir fichier json en liste #####
data = json.loads(json_string)
players_list = data['players']
# ##########################################

def number_of_player():
    nb_players = len(players_list)
    print('the tournament has ' + str(nb_players) + ' players')
    return nb_players





    