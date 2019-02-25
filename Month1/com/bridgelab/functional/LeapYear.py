from com.bridgelab.util import Utility

year = int(input("Enter year : "))
if Utility.is_leap_year(year):
    print("Year is leap year.")
else:
    print("Year is not leap year.")
