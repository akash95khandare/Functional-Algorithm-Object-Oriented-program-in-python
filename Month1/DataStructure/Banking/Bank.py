import time
from DataStructure.Banking.UserInQueue import UserInQueue
from DataStructure.Banking import Services


class Bank:
    def start(self):
        print(" Welcome in sbi ")
        user_in_queue = UserInQueue()
        service = Services()
        user_in_queue.user_in_queue()
        for i in range(user_in_queue.queue.size()):
            cust = user_in_queue.queue.dequeue()
            if cust.get_operation() == 1:
                service.withdraw(cust.get_account_no(), cust.get_amount(), cust.get_customer_name())
            elif cust.get_operation() == 2:
                service.deposit(cust.get_account_no(), cust.get_amount(), cust.get_customer_name())
            elif cust.get_operation() == 3:
                service.account_created()
            print("success")
            time.sleep(1)
        service.write()


if __name__ is '__main__':
    obj = Bank()
    obj.start()
