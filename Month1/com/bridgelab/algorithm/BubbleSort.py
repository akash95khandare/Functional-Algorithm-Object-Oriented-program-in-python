from com.bridgelab.util import Utility as u

arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
stringArr = ["akash", "shubham", "rohan", "sham", "nikhil", "rahul", "arvind"]

start = u.startWatch()
print(u.bubbleSort(arr))
print("Elapse time : ", u.stopWatch(start))

start = u.startWatch()
print(u.bubbleSort(list(stringArr)))
print("Elapse time : ", u.stopWatch(start))