from com.bridgelab.util.Utility import wordList, readFromFile

sts = readFromFile()
print(sts)
key = input("Enter word for search : ")
if wordList(key, sts):
    print("Word found.")
else:
    print("Word not found.")
