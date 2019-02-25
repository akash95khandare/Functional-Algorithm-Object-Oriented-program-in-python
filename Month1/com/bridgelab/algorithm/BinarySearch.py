from array import array

from com.bridgelab.util.Utility import binary_search

arr = array('i', [4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
print(arr)
key = int(input("Enter a key : "))
mid = binary_search(arr, 0, len(arr) - 1, key)
print(mid)
