from com.bridgelab.DataStructure.Banking.Customer import Customer
from com.bridgelab.util.Queue import Queue


class UserInQueue:
    def __init__(self):
        self.queue = Queue()

    def user_in_queue(self):
        n = int(input("how many user want to stay in queue : "))
        for i in range(n):
            cust = Customer()
            acc_no = input("Enter account no : ")
            name = input("Enter name : ")
            amount = int(input("Enter amount : "))
            operation = int(input("Enter \n1 for withdraw \n2 for deposit \n3 for account creation \n"))
            cust.set_amount(amount)
            cust.set_account_no(acc_no)
            cust.set_customer_name(name)
            cust.set_operation(operation)
            self.queue.enqueue(cust)
