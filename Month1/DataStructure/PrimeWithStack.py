from util import Utility
from util.Stack import Stack


class PrimeWithStack:
    def __init__(self):
        """
        Creating object of stack for maintain and store data
        """
        self.stack = Stack()

    def prime_with_stack(self, rng):
        """
        :param rng : Take one input from user as range
        Print prime number between 2 to range
        """
        prime_number = Utility.get_prime_number(rng)
        anagram = Utility.get_anagram(prime_number)
        for i in anagram:
            self.stack.push(i)
        for i in range(self.stack.size()):
            print(self.stack.pop(), end=" ")


if __name__ == '__main__':
    """
        This is main method
        Creating object of PrimeWithStack class and call its method 
    """
    obj = PrimeWithStack()
    rng = int(input("Enter range : "))
    obj.prime_with_stack(rng)
