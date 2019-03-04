from DataStructure.Banking import Customer
from util import Queue


class UserInQueue:
    def __init__(self):
        """
        Creating object of queue class for maintaining customer in queue
        """
        self.queue = Queue()

    def user_in_queue(self):
        """
        Take customer detail from user and store and maintain in queue
        """
        n = int(input("how many user want to stay in queue : "))
        for i in range(n):
            cust = Customer()
            acc_no = input("Enter account no : ").strip()
            name = input("Enter name : ").strip()
            amount = int(input("Enter amount : "))
            operation = int(input("Enter \n1 for withdraw \n2 for deposit \n3 for account creation \n"))
            cust.set_amount(amount)
            cust.set_account_no(acc_no)
            cust.set_customer_name(name)
            cust.set_operation(operation)
            try:
                if operation > 4 or operation < 1:
                    raise ValueError
            except:
                print("Select wrong option.")
                self.user_in_queue()
            else:
                self.queue.enqueue(cust)
