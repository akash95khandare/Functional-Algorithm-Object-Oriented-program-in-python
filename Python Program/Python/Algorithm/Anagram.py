import sys
sys.path.insert(0, '/home/admin1/Desktop/Python Program/Functional')
import Utility as u
str1 = input("Enter first string : ")
str2 = input("Enter second string : ")

if(u.isAnagram(str1,str2)):
	print("Same")
else:
	print("Not")