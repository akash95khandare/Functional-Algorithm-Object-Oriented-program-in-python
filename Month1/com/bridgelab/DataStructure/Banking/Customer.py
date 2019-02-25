class Customer:
    def __init__(self):
        self.account_no = 0.0
        self.customer_name = None
        self.amount = None
        self.operation = None

    def get_account_no(self):
        return self.account_no

    def set_account_no(self, account_no):
        self.account_no = account_no

    def get_customer_name(self):
        return self.customer_name

    def set_customer_name(self, customer_name):
        self.customer_name = customer_name

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    def get_operation(self):
        return self.operation

    def set_operation(self, operation):
        self.operation = operation

    def toString(self):
        return str(self.get_account_no()) + " " + self.get_customer_name() + " " + str(self.get_amount())


# cust = Customer()
# cust.set_account_no("1234")
# cust.set_customer_name("akash")
# cust.set_amount("500.0")
# print(cust.toString())
# cust1 = cust
# cust1.set_amount(800)
# print(cust.toString())
