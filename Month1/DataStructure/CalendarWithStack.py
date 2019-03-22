from DataStructure.Calendar import Calendar
from DataStructure.CalendarWithQueue import CalendarWithQueue


from util.Stack import Stack


class CalendarWithStack:
    def __init__(self):
        """
            Creating two object of stack for storing day of month
        """
        self.stack1 = Stack()
        self.stack2 = Stack()

    def display(self, month, year):
        """
            :param month: take month parameter and display it
            :param year: take year parameter and display it
        """
        calendar = Calendar()
        print("------------", month, year, "---------------")
        for i in calendar.week:
            print(i, end="    ")
        for i in range(self.stack2.size()):
            temp = self.stack2.pop()
            if i % 7 == 0:
                print()
            if int(temp) == 0:
                print(end="     ")
            elif int(temp) < 10:
                print(temp, end="    ")
            else:
                print(temp, end="   ")

    def calendar_with_stack(self, month, year):
        """

            :param m: m as month parameter for calculating month
            :param y: y as year parameter for calculating year
        """
        queue = CalendarWithQueue()
        queue = queue.calendar_with_queue(month, year)
        for i in range(queue.size()):
            self.stack1.push(queue.dequeue())
        for i in range(self.stack1.size()):
            self.stack2.push(self.stack1.pop())


if __name__ == '__main__':
    """
        This is main method
        Creating object of CalendarWithStack class and call its method 
    """
    calendar_with_stack = CalendarWithStack()
    try:
        month = int(input("Enter a month : "))
        if month / 10 > 1.2:
            raise ValueError
    except ValueError:
        print("Month input is invalid.")
    else:
        year = int(input("Enter a year : "))
        calendar_with_stack.calendar_with_stack(month, year)
        calendar_with_stack.display(month, year)
