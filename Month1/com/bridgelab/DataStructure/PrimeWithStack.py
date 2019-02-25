from com.bridgelab.util import Utility
from com.bridgelab.util.Stack import Stack


class PrimeWithStack:
    def __init__(self):
        self.stack = Stack()

    def prime_with_stack(self, rng):
        prime_number = Utility.get_prime_number(rng)
        anagram = Utility.get_anagram(prime_number)
        for i in anagram:
            self.stack.push(i)
        for i in range(self.stack.size()):
            print(self.stack.pop(), end=" ")


obj = PrimeWithStack()
rng = int(input("Enter range : "))
obj.prime_with_stack(rng)
