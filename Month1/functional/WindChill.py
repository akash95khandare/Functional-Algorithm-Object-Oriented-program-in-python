from util import Utility


def main():
    t = int(input("Enter temperature : "))
    v = int(input("Enter wind speed : "))
    print("Wind Chill is : ", Utility.weather(t, v))


if __name__ == '__main__':
    main()
