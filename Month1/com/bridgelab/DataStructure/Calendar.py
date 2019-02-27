from math import trunc
import numpy
from com.bridgelab.util import Utility


class Calendar:
    def __init__(self):
        self.arr = []
        self.week = ["S", "M", "T", "W", "Th", "F", "S"]
        self.month_days = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]

    def display(self, arr):
        # for i in range(7):
        #     for j in range(7):
        #         if i > 0 and arr[i - 1][j] == 0:
        #             print(end="   ")
        #             continue
        #         elif i > 0:
        #             print(int(arr[i - 1][j]), end="   ")
        #             continue
        #         print(self.week[j], end="   ")
        #     # if i > 0:
        #     print()
        print(self.week)


    def initial(self, m, y):
        day_of_year = (y * 365 + trunc((y - 1) / 4) - trunc((y - 1) / 100) +
                       trunc((y - 1) / 400)) % 7
        month = self.month_days[m - 1] + 28
        for i in range(m - 1):
            day_of_year += self.month_days[i]
        if Utility.is_leap_year(y):
            if m == 2:
                month += 1
            day_of_year += 1
        day_of_year %= 7
        temp = 1
        for i in range(42):
            if day_of_year > 0:
                self.arr.append(0)
                day_of_year -= 1
                continue
            if temp <= month:
                self.arr.append(temp)
                temp += 1
        return self.arr


if __name__ == "__main__":
    c = Calendar()
    month = int(input("Enter a month : "))
    year = int(input("Enter a year : "))
    arr = c.initial(month, year)
    c.display(arr)
