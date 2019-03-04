import numpy
from util import Utility as u


class TwoDPrimeArray:
    def __init__(self):
        """
        Creating array for maintain and store data in array
        """
        self.arr = numpy.zeros((10, 168))

    def two_d_prime_array(self, rng):
        """
        :param rng: Take one input as range
        print array of prime number
        """
        number = u.get_prime_number(rng)
        k = j = 0
        block = 100
        for i in number:
            if i > block:
                k += 1
                j = 0
                block += 100
            self.arr[k][j] = i
            j += 1
        for x in range(10):
            for y in range(30):
                if self.arr[x][y]==0:
                    continue
                print(int(self.arr[x][y]), end=" ")
            print()


if __name__ == '__main__':
    """
        This is main method
        Creating object of TwoDPrimeArray class and call its method 
    """
    t = TwoDPrimeArray()
    rng = int(input("Enter range : "))
    try:
        if rng > 1000:
            raise ValueError
    except ValueError:
        print("Range exceeded.")
    else:
        t.two_d_prime_array(rng)
