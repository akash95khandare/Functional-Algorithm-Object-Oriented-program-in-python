def celsiusToFahrenheit(c):
    f = c * 9 / 5 + 32
    return f


def fahrenheitToCelsius(f):
    c = (f - 32) * 5 / 9
    return c


c = int(input("Enter fahrenheit for converting into celsius : "))
print(celsiusToFahrenheit(c))
f = int(input("Enter celsius for converting into fahrenheit : "))
print(fahrenheitToCelsius(f))
