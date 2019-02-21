from com.bridgelab.functional.Utility import insertionSort, binary, bubbleSort, mergeSort


def wordList():
    f = open("abc.txt", 'r')
    word = ""
    for i in f:
        word = word + i
    st = {}
    st = word.split("\n")
    sts = bubbleSort(list(st))
    print(sts)
    mid = binary(sts, 0, len(sts) - 1, "about")
    print(mid)


arr = [5, 4, 12, 78, 56, 1, 2, 3]
print(insertionSort(arr))

print(mergeSort(arr, 0, len(arr) - 1))
print(arr)
wordList()
