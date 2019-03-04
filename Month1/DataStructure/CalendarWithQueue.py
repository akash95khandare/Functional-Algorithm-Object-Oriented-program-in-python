from DataStructure.Calendar import Calendar
from util.Queue import Queue
import numpy


class CalendarWithQueue:
    def __init__(self):
        """
        Creating object of queue for storing day of month
        """
        self.queue = Queue()

    def display(self, month, year):
        """
            :param month: take month parameter and display it
            :param year: take year parameter and display it
        """
        calendar = Calendar()
        print("------------", month, year, "---------------")
        for i in calendar.week:
            print(i, end="    ")
        for i in range(self.queue.size()):
            temp = self.queue.dequeue()
            if i % 7 == 0:
                print()
            if int(temp) == 0:
                print(end="     ")
            elif int(temp) < 10:
                print(temp, end="    ")
            else:
                print(temp, end="   ")

    def calendar_with_queue(self, month, year):
        """
            :param m: m as month parameter for calculating month
            :param y: y as year parameter for calculating year
            :return: return queue of day of month
        """
        calendar = Calendar()
        arr = calendar.initial(month, year)
        arr1 = numpy.array(arr).reshape(6, 7)
        for i in range(6):
            for j in range(7):
                self.queue.enqueue(arr1[i][j])
        return self.queue


if __name__ == '__main__':
    """
        This is main method
        Creating object of CalendarWithQueue class and call its method 
    """
    calendar_with_queue = CalendarWithQueue()
    month = int(input("Enter a month : "))
    try:
        if month / 10 > 1.2:
            raise ValueError
    except ValueError:
        print("Month input is invalid.")
    else:
        year = int(input("Enter a year : "))
        calendar_with_queue.calendar_with_queue(month, year)
        calendar_with_queue.display(month, year)
