
class Match:

    #def __init__(self, name):
    def __init__(self, name, array):
        self._name = name
        self._array = array
    
#-----------------------------------------------------------------------
#        Methods
#-----------------------------------------------------------------------

   
    @property
    def match_name(self):
        print(f'{self._name}" was accessed.')
        return self._name

    @match_name.setter
    def match_name(self, value):
        print(f'{self._name} is now "{value}"')
        self._name = value

    @match_name.deleter
    def match_name(self):
        print(f'"{self._name}" was deleted')

    
# def add
# def getAll
# def get
# def update
# def delete


# class Match :
#     def __init__(self, name):
#         self.name = name

    # def store_score(self):
    #     match = []
        # player 1 score : 1
        # player 2 score : 0
        # tuple1 = []
        # tuple1.append(player1)
        # tuple1.append(score)
        # tuple2.append(player2)
        # tuple2.append(score)
        # match.append(tuple1)
        # match.append(tuple2)




        







################################################################################################
########## On récupère les résultats pour chaque matchs  ##########
############################################################################

# tour_length = len(tour)

# nextTourArray = [] #tableau des joueurs qualifiés pour le prochain tour


# for x in range(tour_length):
#     print('match numéro ' + str(x + 1))
#     print(tour[x])
#     while True:         
#         print("Qui a gagné ce match ? Joueur 1 ou joueur 2 ? [1/2]")    
#         data = input()   
#         if data == '1' or data == '2' :
#             print('ce joueur sera retenu')
#             print(tour[x][int(data)])
#             nextTourArray.append(tour[x][int(data)])
#             print(' ')
#             break
#         else:
#             print('réponse invalide')
#     x = x + 1

# print(nextTourArray)

# number_of_players = len(nextTourArray)
# #print(number_of_players)

# number_of_pairs = round(number_of_players / 2)
# #print(number_of_pairs)


# y = 1
# secondTour = []
# for x in range(number_of_pairs):
#     matchName = str('Match' + str(y))
#     newMatch = []
#     newMatch.append(matchName)
#     for i in range(2):
#         choosen_player = random.choice(nextTourArray)
#         newMatch.append(choosen_player)
#         nextTourArray.remove(choosen_player)
#         i = i + 1
#     secondTour.append(newMatch)
#     print(newMatch)
#     y = y + 1
# print(' ')
# print('second tour')
# print(secondTour)



