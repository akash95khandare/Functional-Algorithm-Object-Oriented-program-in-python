from com.bridgelab.util.DeQueue import DeQueue


class PalindromeChecker:
    def __init__(self):
        self.dequeue = DeQueue()

    def palindromeChecker(self, string):
        for i in range(len(string)):
            self.dequeue.enqueue_from_rear(string[i])
        while self.dequeue.size() > 1:
            if self.dequeue.dequeue_from_front() != self.dequeue.dequeue_from_rear():
                return False
        return True


p = PalindromeChecker()
res = p.palindromeChecker("toot")
print(res)
