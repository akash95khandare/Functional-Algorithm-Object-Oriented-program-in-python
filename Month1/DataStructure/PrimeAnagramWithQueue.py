from util.Queue import Queue
from util import Utility


class PrimeAnagramWithQueue:
    def __init__(self):
        """
        Creating object of queue for maintain and store data
        """
        self.queue = Queue()

    def prime_anagram_with_queue(self, rng):
        """
        :param rng: take one parameter range for calculating prime anagram from 1 to range
        print prime anagram number on console
        """
        prime_number = Utility.get_prime_number(rng)
        anagram_number = Utility.get_anagram(prime_number)
        for i in anagram_number:
            self.queue.enqueue(i)
        for i in range(self.queue.size()):
            print(self.queue.dequeue(), end=" ")


if __name__ == '__main__':
    """
        This is main method
        Creating object of PrimeAnagramWithQueue class and call its method 
    """
    obj = PrimeAnagramWithQueue()
    rng = int(input("Enter range : "))
    obj.prime_anagram_with_queue(rng)
