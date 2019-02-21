import com.bridgelab.functional.Utility as u

arr = [5, 4, 8, 9, 36, 14, 474]
start = u.startWatch()
print(u.insertionSort(arr))
print("Elapse time : ", u.stopWatch(start))
