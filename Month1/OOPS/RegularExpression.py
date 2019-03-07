from re import search


class RegularExpression:
    def __init__(self, string):
        self.string = string

    def regular_expression(self):

        patt = search("<+.{4}>+", self.string)
        name = input("Enter name : ")
        self.replace_string(patt.group(), name)

        patt = search("<+.{9}>+", self.string)
        name = input("Enter full name : ")
        self.replace_string(patt.group(), name)

        patt = search("x{10}", self.string)
        name = input("Enter mobile number : ")
        self.replace_string(patt.group(), name)

        patt = search("xx\Sxx\Sx{4}", self.string)
        name = input("Enter date : ")
        self.replace_string(patt.group(), name)
        print(self.string)

    def replace_string(self, patt, word):
        self.string = self.string.replace(patt, word)


if __name__ == '__main__':
    string = "Hello <<name>>, We have your full" \
             + "name as <<full name>> in our system. your contact number is 91­xxxxxxxxxx." \
             + "Please,let us know in case of any clarification Thank you BridgeLabz xx/xx/xxxx."
    regular_exp = RegularExpression(string)
    regular_exp.regular_expression()
