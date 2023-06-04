from players import json_string
import json
import random 

data = json.loads(json_string)
players_list = data['players']

# count = 0
# for players in data['players']: 
#     #print(data['players'][count])
#     count = count + 1

number_of_players = len(players_list)
#print(number_of_players)

number_of_pairs = round(number_of_players / 2)
#print(number_of_pairs)


for x in range(number_of_pairs ):
    newMatch = []
    for i in range(2):
        choosen_player = random.choice(players_list)
        newMatch.append(choosen_player)
        players_list.remove(choosen_player)
        i = i + 1
    print(newMatch)














