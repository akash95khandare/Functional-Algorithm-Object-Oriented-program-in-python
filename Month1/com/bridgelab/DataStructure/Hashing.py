from com.bridgelab.util.IO import readFromFile, append
from com.bridgelab.util.LinkedList import LinkedList


class Hashing:
    def __init__(self):
        self.list = []

    def display_hash(self):
        for i in range(11):
            if self.list[i].is_empty():
                continue
            print(i, " = ", end="")
            self.list[i].display()
            print()

    def get_number(self):
        n = input("Enter number : ")
        res = int(n) % 11
        if self.list[res].search(n):
            self.list[res].remove(n)
        else:
            self.list[res].sort(n)

    def hashing(self):
        for i in range(11):
            self.list.append(LinkedList())
        number = readFromFile("number.txt")
        for i in range(len(number)-1):
            res = int(number[i]) % 11
            self.list[res].sort(number[i])
        self.display_hash()
        self.get_number()
        self.display_hash()
        f = open("number.txt", 'r+')
        f.truncate()
        for i in range(11):
            if self.list[i].is_empty():
                continue
            append("number.txt", self.list[i])


h = Hashing()
h.hashing()
