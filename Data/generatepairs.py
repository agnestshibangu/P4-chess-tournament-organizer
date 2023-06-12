from playersgenpairs import json_string
import json
import random 

################################################################################################
########## On génère les paires à partir de la liste des players dans le fichier JSON ##########
################################################################################################

data = json.loads(json_string)
players_list = data['players']


number_of_players = len(players_list)
#print(number_of_players)

number_of_pairs = round(number_of_players / 2)
#print(number_of_pairs)

tour = []

y = 1
for x in range(number_of_pairs):
    matchName = str('Match' + str(y))
    newMatch = []
    newMatch.append(matchName)
    for i in range(2):
        choosen_player = random.choice(players_list)
        newMatch.append(choosen_player)
        players_list.remove(choosen_player)
        i = i + 1
    tour.append(newMatch)
    print(newMatch)
    y = y + 1
print(' ')
# print(tour)



################################################################################################
########## On récupère les résultats pour chaque matchs  ##########
################################################################################################

tour_length = len(tour)

nextTourArray = [] #tableau des joueurs qualifiés pour le prochain tour


for x in range(tour_length):
    print('match numéro ' + str(x + 1))
    print(tour[x])
    while True:         
        print("Qui a gagné ce match ? Joueur 1 ou joueur 2 ? [1/2]")    
        data = input()   
        if data == '1' or data == '2' :
            print('ce joueur sera retenu')
            print(tour[x][int(data)])
            nextTourArray.append(tour[x][int(data)])
            print(' ')
            break
        else:
            print('réponse invalide')
    x = x + 1

print(nextTourArray)

number_of_players = len(nextTourArray)
#print(number_of_players)

number_of_pairs = round(number_of_players / 2)
#print(number_of_pairs)


y = 1
secondTour = []
for x in range(number_of_pairs):
    matchName = str('Match' + str(y))
    newMatch = []
    newMatch.append(matchName)
    for i in range(2):
        choosen_player = random.choice(nextTourArray)
        newMatch.append(choosen_player)
        nextTourArray.remove(choosen_player)
        i = i + 1
    secondTour.append(newMatch)
    print(newMatch)
    y = y + 1
print(' ')
print('second tour')
print(secondTour)



