from util.Utility import root_of_x


def main():
    print("find the roots of the equation a*x*x + b*x + c")
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    c = int(input("Enter c : "))
    x1, x2 = root_of_x(a, b, c)
    print("Root 1 of x : ", int(x1), "\nRoot 2 of x : ", int(x2))


if __name__ == '__main__':
    main()
