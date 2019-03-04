from util.IO import read_from_file, append
from util.LinkedList import LinkedList


class Hashing:
    def __init__(self):
        """
        Creating empty list for storing
        """
        self.list = []

    def display_hash(self):
        """
        Display data from linked list on console
        """
        for i in range(11):
            if self.list[i].is_empty():
                continue
            print(i, " = ", end="")
            self.list[i].display()
            print()

    def get_number(self):
        """
        Take one input from user and check number present or not
        If found then delete that number from respective linked list
        If not found then add number in respective linked list object by calculating hash
        """
        n = input("Enter number : ")
        res = int(n) % 11
        if self.list[res].search(n):
            self.list[res].remove(n)
        else:
            self.list[res].sort(n)

    def hashing(self):
        """
        Creating 11 linked list object for storing data and
        maintain 11 object of linked list in the list
        @read_from_file method call for reading data from number.txt and
        store data in respective linked list object by calculating hash
        Perform operation on object of linked list
        @append method call for storing data into file as number.txt
        """
        for i in range(11):
            self.list.append(LinkedList())
        number = read_from_file("number.txt")
        for i in range(len(number) - 1):
            res = int(number[i]) % 11
            self.list[res].sort(number[i])
        self.display_hash()
        self.get_number()
        self.display_hash()

        try:
            f = open("number.txt", 'r+')
        except IOError:
            print("number.txt file not found.")
        else:
            f.truncate()
            for i in range(11):
                if self.list[i].is_empty():
                    continue
                append("number.txt", self.list[i])


if __name__ == '__main__':
    """
        This is main method
        Creating object of Hashing class and call its method 
    """
    h = Hashing()
    h.hashing()
