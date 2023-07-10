class Match:
    '''This is a class method for creating a match has two attributes : a name and an array
    of tuples wich contains the infos of the players. It has some getter/setter properties
    to access, set and delete the name and the array for every match.
    '''
    def __init__(self, name, array):
        self._name = name
        self._array = array

    @property
    def match_name(self):
        # print(f'{self._name}" was accessed.')
        return self._name

    @match_name.setter
    def match_name(self, value):
        # print(f'{self._name} is now "{value}"')
        self._name = value

    @match_name.deleter
    def match_name(self):
        print(f'"{self._name}" was deleted')

    @property
    def match_array(self):
        # print(f'{self._name}" was accessed.')
        return self._array

    @match_array.setter
    def match_array(self, value):
        # print(f'{self._name} is now "{value}"')
        self._array = value

    @match_array.deleter
    def match_array(self):
        print(f'"{self._array}" was deleted')
