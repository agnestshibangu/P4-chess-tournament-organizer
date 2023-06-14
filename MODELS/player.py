class Player:

    def __init__(self, number, score : int):
    # def __init__(self, familyName, firstName, birthDate, NationalIdentifier):
        self._number = number
        self._score = score
        # self._firstName = firstName
        # self._birthDate = birthDate
        # self._NationalIdentifier = NationalIdentifier
  
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------

    @property
    def player_score(self):
        print(f'{self._score}" was accessed.')
        return self._score

    @player_score.setter
    def player_score(self, value):
        print(f'{self._score} is now "{value}"')
        self._score = value

    @player_score.deleter
    def player_score(self):
        print(f'"{self._score}" was deleted')
        del self._score


player = Player('player_n°', 5)
player.player_score
del player.player_score
player.pleeeeeeeeee
