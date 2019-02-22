from array import array
from com.bridgelab.util.Utility import mergeSort, startWatch, stopWatch

arr = array('i', [56, 35, 4, 99, 98, 77, 3, 2, 1, 0])
stringArr = ["akash", "shubham", "rohan", "sham", "nikhil", "rahul", "arvind"]

start = startWatch()
mergeSort(arr, 0, len(arr) - 1)
print(arr)
print("Elapse time : ", stopWatch(start))

start = startWatch()
print(mergeSort(stringArr, 0, len(arr) - 1))
print("Elapse time : ", stopWatch(start))
