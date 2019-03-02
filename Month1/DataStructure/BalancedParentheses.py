from util.Stack import Stack


class BalancedParentheses:
    def __init__(self):
        """
        Creating object of stack class
        """
        self.stack = Stack()

    def balancedParentheses(self, string):
        """
        :param string : take one input:
        :return : return true if string is balanced else false
        """
        for i in string:
            if i is '(':
                self.stack.push(i)
            elif i is ')' and self.stack.peak() is '(':
                self.stack.pop()

        if self.stack.size() is 0:
            return True
        else:
            return False


if __name__ == "__main__":
    """
    This is main method
    Creating object of BalancedParentheses class and call its method 
    """
    obj = BalancedParentheses()
    string = "(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)"
    result = obj.balancedParentheses(string)
    print(result)