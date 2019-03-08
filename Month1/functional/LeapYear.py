from util import Utility


def main():
    year = int(input("Enter year : "))
    if Utility.is_leap_year(year):
        print("Year is leap year.")
    else:
        print("Year is not leap year.")


if __name__ == '__main__':
    main()
