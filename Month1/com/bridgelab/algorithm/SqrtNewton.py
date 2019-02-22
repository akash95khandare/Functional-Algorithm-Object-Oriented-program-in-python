import math


def sqrt(c):
    t = c
    t = (c / t + t) / 2
    epsilon = math.e - 15
    if abs(t - c / t) > epsilon * t:
        print(epsilon * t)


n = int(input("Enter number : "))
sqrt(n)
