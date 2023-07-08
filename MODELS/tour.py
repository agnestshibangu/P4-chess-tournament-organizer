class Tour:
    '''This is a class method for creating a tour that has 7 attributes attributes : a name, a date,
    a number of matches, an array of matches, a start time and an end time. It has some getter/setter properties
    to access, set and delete the mentionned attributes above.
    '''

    def __init__(self, name, date, number_of_matchs, array_of_matches, start_time, end_time):
        self._name = name
        self._date = date
        self._number_of_matchs = number_of_matchs
        self._array_of_matches = array_of_matches
        self._start_time = start_time
        self._end_time = end_time

    # NAME
    @property
    def tour_name(self):
        print(f'"{self._name}" was accessed.')
        return self._name

    @tour_name.setter
    def tour_name(self, value):
        # print(f'{self._name} is now "{value}"')
        self._name = value

    # DATE
    @property
    def tour_date(self):
        # print(f'"{self._date}" was accessed.')
        return self._date

    @tour_date.setter
    def tour_date(self, value):
        print(f'{self._date} is now "{value}"')
        self._date = value
   






    # NUMBER OF MATCHES
    @property
    def tour_number_of_matchs(self):
        # print(f'"{self._number_of_matchs }" was accessed.')
        return self._number_of_matchs

    @tour_number_of_matchs.setter
    def tour_number_of_matchs(self, value):
        # print(f'{self._number_of_matchs } is now "{value}"')
        self._number_of_matchs = value


    @property
    def tour_number_of_matchs(self):
        # print(f'"{self._number_of_matchs }" was accessed.')
        return self._number_of_matchs

    @tour_number_of_matchs.setter
    def tour_number_of_matchs(self, value):
        # print(f'{self._number_of_matchs } is now "{value}"')
        self._number_of_matchs = value


    @property
    def tour_number_of_matchs(self):
        # print(f'"{self._number_of_matchs }" was accessed.')
        return self._number_of_matchs

    @tour_number_of_matchs.setter
    def tour_number_of_matchs(self, value):
        # print(f'{self._number_of_matchs } is now "{value}"')
        self._number_of_matchs = value