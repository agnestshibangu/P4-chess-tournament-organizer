class Match:

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

    