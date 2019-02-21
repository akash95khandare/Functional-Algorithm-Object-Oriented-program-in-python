import math

principle = int(input("Enter principle : "))
year = int(input("How many year  :"))
rate = int(input("Enter rate of interest : "))


def monthlyPayment(principle, year, rate):
    n = 12 * year
    r = rate / (12 * 100)
    payment = (principle * r) / 1 - math.pow((1 + r), -n)
    return payment


print(monthlyPayment(principle, year, rate))
