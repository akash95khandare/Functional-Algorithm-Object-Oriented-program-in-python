from com.bridgelab.util.Stack import Stack


class BalancedParentheses:
    def __init__(self):
        self.stack = Stack()

    def balancedParentheses(self, string):
        for i in string:
            if i is '(':
                self.stack.push(i)
            elif i is ')' and self.stack.peak() is '(':
                self.stack.pop()

        if self.stack.size() is 0:
            return True
        else:
            return False


obj = BalancedParentheses()
string = "(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)"
result = obj.balancedParentheses(string)
print(result)