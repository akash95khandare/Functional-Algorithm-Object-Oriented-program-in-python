import sys
sys.path.insert(0,'/home/admin1/Desktop/Python Program/Functional')
import Utility as u

arr = [5,4,8,9,36,14,474]
start = u.startWatch()
print(u.insertionSort(arr))
print("Elapse time : ",u.stopWatch(start))