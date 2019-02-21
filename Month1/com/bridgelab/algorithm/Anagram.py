import com.bridgelab.functional.Utility as u

str1 = input("Enter first string : ")
str2 = input("Enter second string : ")

if u.isAnagram(str1, str2):
    print("Same")
else:
    print("Not")
