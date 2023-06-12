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

    def __init__(self, name, number_of_matchs):
        self._name = name
        self._number_of_matchs = number_of_matchs

#-----------------------------------------------------------------------
#        Methods
#-----------------------------------------------------------------------

    @property
    def tour_name(self):
        print(f'"{self._name}" was accessed.')
        return self._name

# def add
# def getAll
# def get
# def update
# def delete





        




