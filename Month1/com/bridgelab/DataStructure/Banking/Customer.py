class Customer:
    def __init__(self):
        self.account_no = 0
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

    def to_string(self):
        return str(self.get_account_no()) + " " + self.get_customer_name() + " " + str(self.get_amount())
