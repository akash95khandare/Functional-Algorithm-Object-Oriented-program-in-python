from com.bridgelab.util.Queue import Queue
from com.bridgelab.util import Utility


class PrimeAnagramWithQueue:
    def __init__(self):
        self.queue = Queue()

    def prime_anagram_with_queue(self, rng):
        prime_number = Utility.get_prime_number(rng)
        anagram_number = Utility.get_anagram(prime_number)
        for i in anagram_number:
            self.queue.enqueue(i)
        for i in range(self.queue.size()):
            print(self.queue.dequeue(), end=" ")


obj = PrimeAnagramWithQueue()
rng = int(input("Enter range : "))
obj.prime_anagram_with_queue(rng)