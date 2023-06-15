from MODELS.playersData import json_string

import sys
import json
# ######################################

# ##### convertir fichier json en liste #####
data = json.loads(json_string)
players_list = data['players']
# ##########################################

def start_tournament():
    while True:         
        print("Voulez-vous démarrer un tournoi ? [Y/N]")    
        data = input()   
        if data == 'Y':
            print('starting a new tournament...')
            break
        elif data == 'N':
            print('good bye !')
            sys.exit()
        else:
            print('invalide answer')
    # créer un objet tournoi


def number_of_player():
    nb_players = len(players_list)
    print('the tournament has ' + str(nb_players) + ' players')
    return nb_players



    