from array import array

from com.bridgelab.functional.Utility import binary

arr = array('i', [4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
key = int(input("Enter a key : "))
mid = binary(arr, 0, len(arr) - 1, key)
print(mid)
