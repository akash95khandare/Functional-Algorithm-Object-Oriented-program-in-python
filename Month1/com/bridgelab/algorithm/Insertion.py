import com.bridgelab.util.Utility as u

arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
stringArr = ["akash", "shubham", "rohan", "sham", "nikhil", "rahul", "arvind"]

start = u.startWatch()
print(u.insertionSort(arr))
print("Elapse time : ", u.stopWatch(start))

start = u.startWatch()
print(u.insertionSort(list(stringArr)))
print("Elapse time : ", u.stopWatch(start))