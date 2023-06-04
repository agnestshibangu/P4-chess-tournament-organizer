import os
import datetime

def Horodatage():
    x = datetime.datetime.now()
    year = str(x.year)
    month = str(x.month)
    day = str(x.day)
    currentDate = year + '-' + month + '-' + day
    return str(currentDate)
    
Horodatage()

currentDate = Horodatage()

folder = str('../Data/new-tournament/' + 'currentDate' + '/')
file = 'file.py'
print(folder)
if not os.path.exists(folder):
    os.makedirs(folder)
open('../Data/new-tournament/currentDate/myfile.py', "x")

    

class Tournament:
    def __init__(self, length, width, color="red"):
        self.length = length
        self.width = width
        self.color = color

    def start_tournament():
        print('start tournament')






