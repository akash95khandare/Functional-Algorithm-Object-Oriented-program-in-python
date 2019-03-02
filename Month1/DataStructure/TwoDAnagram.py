import numpy
from util import Utility


class TwoDAnagram:
    def __init__(self):
        self.arr = numpy.full((2, 800), 0)

    def two_d_anagram(self, rng):
        prime_number = Utility.get_prime_number(rng)
        b_value = True
        cnt = 0
        for i in range(len(prime_number)):
            for j in range(len(prime_number)):
                if i == j:
                    continue
                b_value = True
                if Utility.is_anagram(str(prime_number[i]), str(prime_number[j])):
                    self.arr[0][cnt] = prime_number[i]
                    self.arr[0][cnt + 1]
                    cnt += 1
                    b_value = False
                    break
            if b_value:
                self.arr[1][i] = prime_number[i]
        print(self.arr)


if __name__ == '__main__':
    obj = TwoDAnagram()
    rng = int(input("Enter range : "))
    obj.two_d_anagram(rng)
