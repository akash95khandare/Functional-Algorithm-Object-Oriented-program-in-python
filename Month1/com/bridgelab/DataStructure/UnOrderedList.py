from com.bridgelab.util import IO
from com.bridgelab.util.LinkedList import LinkedList


class UnOrderedList:

    def __init__(self):
        self.list = LinkedList()

    def unorderedList(self):
        word = IO.readFromFile("abc.txt")
        for j in word:
            self.list.add(j)
        self.list.display()
        w = input('\nEnter word :')
        if self.list.search(w):
            self.list.remove(w)
            print("Removed")
        else:
            self.list.add(w)
            print("Added")
        self.list.display()
        IO.writeToFile("abc.txt", self.list)


obj = UnOrderedList()
obj.unorderedList()
