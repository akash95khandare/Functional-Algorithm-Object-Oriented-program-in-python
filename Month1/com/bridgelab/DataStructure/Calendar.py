import numpy
from com.bridgelab.util import Utility


class Calendar:
    def __init__(self):
        self.arr = numpy.empty((6, 7))
        self.week = ["S", "M", "T", "W", "Th", "F", "S"]
        self.week_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.start_day = 2
        self.month = 1
        self.year = 2019

    def initial(self, m, y):
        year = self.year
        counter = 0
        temp_y = self.year

        while y > year:
            if counter == 7:
                counter = 0
            year -= 1
            if Utility.is_leap_year(year):
                counter += 2
            else:
                counter += 1

        counter = self.start_day
        while y < temp_y:
            temp_y -= 1
            if counter == 0:
                counter = 7
            if Utility.is_leap_year(year):
                counter -= 2
            else:
                counter -= 1
        return counter


c = Calendar()
print(c.initial(2, 2019))
