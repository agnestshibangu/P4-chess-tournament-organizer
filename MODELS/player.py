class Player:

    def __init__(self, number : int, score : int, matches_history):
    # def __init__(self, familyName, firstName, birthDate, NationalIdentifier):
        self._number = number
        self._score = score
        # self._firstName = firstName
        # self._birthDate = birthDate
        # self._NationalIdentifier = NationalIdentifier
  
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------

    # getter setter for number

    @property
    def player_number(self):
        print(f'{self._number}" number was accessed.')
        return self._number

    @player_number.setter
    def player_number(self, value):
        print(f'{self._number} is now "{value}"')
        self._number = value

    @player_number.deleter
    def player_number(self):
        print(f'"{self._number}" was deleted')
        del self._number

    
    # getter setter for score

    @property
    def player_score(self):
        print(f'"{self._score}" player s score was accessed.')
        return self._score
    
    @player_score.setter
    def player_score(self, value):
        print(f'{self._score} is now "{value}"')
        self._score = value
    
    # getter setter for history, an array that stores already encoutered players
    @property
    def player_history(self):
        print(f'"{self._history}" player s score was accessed.')
        return self._history
    
    @player_history.setter
    def player_history(self, value):
        print(f'{self._history} is now "{value}"')
        self._history = value


    
    
    
