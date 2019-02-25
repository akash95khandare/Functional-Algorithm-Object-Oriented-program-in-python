def readFromFile(filename):
    f = open(filename, 'r+')
    j = ""
    for i in f:
        j = i + j
    word = j.split(" ")
    return word


def writeToFile(filename, ls):
    f = open(filename, 'w')
    size = ls.size()
    for i in range(size):
        f.write(ls.poll_first() + " ")


def append(filename, ls):
    f = open(filename, 'a')
    size = ls.size()
    for i in range(size):
        f.write(ls.poll_first() + " ")
