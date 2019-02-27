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
        arr1 = numpy.array(arr).reshape(6, 7)
        for i in arr1:
            self.queue.enqueue(i)
        for i in range(self.queue.size()):
            if i < 7:
                print(" ", end=" ")
            print(self.queue.dequeue())


calendar_with_queue = CalendarWithQueue()
month = int(input("Enter a month : "))
year = int(input("Enter a year : "))
calendar_with_queue.calendar_with_queue(month, year)
