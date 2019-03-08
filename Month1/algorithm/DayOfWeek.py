from util.Utility import day_of_week


def main():
    day = int(input("Enter a day : "))
    month = int(input("Enter a month : "))
    year = int(input("Enter a year : "))

    print(day_of_week(day, month, year))


if __name__ == '__main__':
    main()
