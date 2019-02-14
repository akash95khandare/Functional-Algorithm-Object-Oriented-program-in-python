import sys
sys.path.insert(0,'/home/admin1/Desktop/Python Program/Functional')
import Utility as u 
range=int(input("Enter range : "))
arr = u.getPrimeNumber(range)
print(arr)
print(u.getPalindrome(arr))
print(u.getAnagram(arr))
