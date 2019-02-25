from com.bridgelab.DataStructure.Banking.UserInQueue import UserInQueue
from com.bridgelab.DataStructure.Banking.Services import Services


class Bank:
    def start(self):
        print(" Welcome in sbi ")
        user_in_queue = UserInQueue()
        service = Services()
        user_in_queue.user_in_queue()
        for i in range(user_in_queue.queue.size()):
            cust = user_in_queue.queue.dequeue()
            if cust.get_operation() == 1:
                service.withdraw(cust.get_account_no, cust.get_amount)
            elif cust.get_operation() == 2:
                service.deposit(cust.get_account_no, cust.get_amount)
            elif cust.get_operation() == 3:
                service.account_created()
        service.write()


obj = Bank()
obj.start()
