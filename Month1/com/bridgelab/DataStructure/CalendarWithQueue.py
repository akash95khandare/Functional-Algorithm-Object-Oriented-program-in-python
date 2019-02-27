from array import array

from com.bridgelab.DataStructure.Calendar import Calendar
from com.bridgelab.util.Queue import Queue
import numpy


class CalendarWithQueue:
    def __init__(self):
        self.queue = Queue()
        self.arr = numpy.array((6, 7))

    def calendar_with_queue(self, month, year):
        calendar = Calendar()
        arr = calendar.initial(month, year)
        print(arr)
        # self.arr = arr
        # print(calendar.arr)
        # print(self.arr.dtype)
        # print(self.arr)
        # for i in len(calendar.arr):
        #     print(int(i))


# calendar_with_queue = CalendarWithQueue()
# month = int(input("Enter a month : "))
# year = int(input("Enter a year : "))
# calendar_with_queue.calendar_with_queue(month, year)
arr = numpy.array([2, 3, 54, 7, 89, 9, 0, 76, 5, 55, 4, 44])
print(arr.reshape(3, 4))
