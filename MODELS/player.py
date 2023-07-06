class Player:

    def __init__(self, number: int, score: int, matches_history: list):
    # def __init__(self, familyName, firstName, birthDate, NationalIdentifier):
        self._number = number
        self._score = score
        self._matches_history = matches_history
        # self._firstName = firstName
        # self._birthDate = birthDate
        # self._NationalIdentifier = NationalIdentifier

    @property
    def player_number(self):
        # print(f'{self._number}" number was accessed.')
        return self._number

    @player_number.setter
    def player_number(self, value):
        # print(f'{self._number} is now "{value}"')
        self._number = value

    @player_number.deleter
    def player_number(self):
        # print(f'"{self._number}" was deleted')
        del self._number
    
    @property
    def player_score(self):
        # print(f'"{self._score}" player s score was accessed.')
        return self._score

    @player_score.setter
    def player_score(self, value):
        # print(f'{self._score} is now "{value}"')
        self._score = value

    # getter setter for history, an array that stores already encoutered players
    @property
    def player_matches_history(self):
        # print(f'"{self._matches_history}" player s matches history was accessed.')
        return self._matches_history

    @player_matches_history.setter
    def player_matches_history(self, value):
        # print(f'{self._matches_history} is now "{value}"')
        self._matches_history = value


    
    
    
