from util import IO
from util.LinkedList import LinkedList


class UnOrderedList:

    def __init__(self):
        """
        Creating object of linked list for maintain and store data
        """
        self.list = LinkedList()

    def unorderedList(self):
        """
            Read data from file and store in linked list
            @read_from_file method call for reading data from file
            Take one input from user and search in linked list
            If data found in linked list then remove that data from linked list
            If not found then add that data into linked list.
            Write data from linked list into abc.txt file
            @write_from_file method call for writing data into abc.txt file
        """
        word = IO.read_from_file("abc.txt")
        for j in word:
            self.list.add(j)
        self.list.display()
        w = input('\nEnter word :').strip()
        if self.list.search(w):
            self.list.remove(w)
            print("Removed")
        else:
            self.list.add(w)
            print("Added")
        self.list.display()
        IO.write_to_file("abc.txt", self.list)


if __name__ == '__main__':
    """
        This is main method
        Creating object of UnOrderedList class and call its method 
    """
    obj = UnOrderedList()
    obj.unorderedList()
