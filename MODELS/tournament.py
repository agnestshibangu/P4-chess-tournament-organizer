#### importer liste de joueurs #####
# from MODELS.playersData import json_string
# import json

# import sys
# import os
# import datetime

######################################

##### convertir fichier json en liste #####
# data = json.loads(json_string)
# players_list = data['players']
###########################################

# class Tournament:
   
#     def __init__(self, name, place, startDate, endDate, current_tour_number, list_of_tours, registered_players_list, 
#         notes_description, number_of_tours="4"):
#         self.name = name
#         self.place = place
#         self.startDate = startDate
#         self.endDate = endDate
#         self.current_tour_number = current_tour_number
#         self.list_of_tours = list_of_tours
#         self.registered_players_list = registered_players_list
#         self.notes_description = notes_description
#         self.number_of_tours = number_of_tours

class Tournament:

    def __init__(self, name:str, number_of_players):
        self._name = name
        self._number_of_players = number_of_players

#-----------------------------------------------------------------------
#        Methods
#-----------------------------------------------------------------------

    @property
    def tournament_name(self):
        # print(f'"{self._name}" was accessed.')
        return self._name

    @tournament_name.setter
    def tournament_name(self, value):
        # print(f'{self._name} is now "{value}"')
        self._name = value

    @tournament_name.deleter
    def tournament_name(self):
        print(f'"{self._name}" was deleted')

    
    @property
    def tournament_number_of_players(self):
        # print(f'"{self._number_of_players}" was accessed.')
        return self._number_of_players

    @tournament_number_of_players.setter
    def tournament_number_of_players(self, value):
        # print(f'{self._number_of_players} is now "{value}"')
        self._number_of_players = value





# def add
# def getAll
# def get
# def update
# def delete


    
    
    










