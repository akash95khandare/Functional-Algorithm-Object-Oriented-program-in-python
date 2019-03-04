from util.DeQueue import DeQueue


class PalindromeChecker:
    def __init__(self):
        """
        Creating object of Dequeue for maintain and storing data
        """
        self.dequeue = DeQueue()

    def palindromeChecker(self, string):
        """
        :param string : take input string as parameter for checking string is palindrome or not
        :return: return boolean value, If string is palindrome then return true else return false
        """
        for i in range(len(string)):
            self.dequeue.enqueue_from_rear(string[i])
        while self.dequeue.size() > 1:
            if self.dequeue.dequeue_from_front() != self.dequeue.dequeue_from_rear():
                return False
        return True


if __name__ == '__main__':
    """
        This is main method
        Creating object of PalindromeChecker class and call its method 
    """
    p = PalindromeChecker()
    string = input("Enter string : ").strip()
    res = p.palindromeChecker(string)
    if res:
        print("String is palindrome.")
    else:
        print("String is not palindrome.")
