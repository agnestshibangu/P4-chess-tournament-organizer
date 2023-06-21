# from MODELS.playersData import json_string

# import json
# import random 

# ######################################

# ##### convertir fichier json en liste #####
# data = json.loads(json_string)
# players_list = data['players']
# ###########################################


# class Tour:

#     def __init__(self, name, date, match_list, startTime, endTime):
#         self.name = name
#         self.date = date
#         self.match_list = match_list
#         self.startTime = startTime
#         self.endTime = endTime

class Tour:

    def __init__(self, name, number_of_matchs, array_of_matches):
        self._name = name
        self._number_of_matchs = number_of_matchs
        self._array_of_matches = array_of_matches

#-----------------------------------------------------------------------
#        Methods
#-----------------------------------------------------------------------

    @property
    def tour_name(self):
        print(f'"{self._name}" was accessed.')
        return self._name
    
    @tour_name.setter
    def tour_name(self, value):
        print(f'{self._name} is now "{value}"')
        self._name = value

    
    @property
    def tour_number_of_matchs(self):
        print(f'"{self._number_of_matchs }" was accessed.')
        return self._number_of_matchs 
    
    @tour_number_of_matchs.setter
    def tour_number_of_matchs (self, value):
        print(f'{self._number_of_matchs } is now "{value}"')
        self._number_of_matchs = value


# def add
# def getAll
# def get
# def update
# def delete





        




