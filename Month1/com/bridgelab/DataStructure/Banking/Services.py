from com.bridgelab.DataStructure.Banking import GetAndStore
from com.bridgelab.DataStructure.Banking.Customer import Customer
from com.bridgelab.util.LinkedList import LinkedList


class Services:
    def __init__(self):
        self.user_list = LinkedList()
        GetAndStore.data_transfer_file_to_list(self.user_list)

    def account_created(self):
        account_no = int(input("Enter account number : "))
        customer_name = input("Enter customer name : ")
        obj = Customer()
        obj.set_amount(0.0)
        obj.set_customer_name(customer_name)
        obj.set_account_no(account_no)
        self.user_list.add(obj)

    def get_data(self, account_no):
        head = self.user_list.get_head()
        while head.object.get_account_no != account_no:
            head = head.next
            if head == None:
                return -1
        return head.obj

    def withdraw(self, account_no, amount):
        obj = self.get_data(account_no)
        if obj == -1:
            self.account_created()
            return
        obj.set_amount(obj.get_amount() + amount)

    def deposit(self, account_no, amount):
        obj = self.get_data(account_no)
        if obj == -1:
            self.account_created()
            return
        obj.set_amount(obj.get_amount() + amount)

    def write(self):
        GetAndStore.data_transfer_list_to_file(self.user_list)
# obj = Services()
# data_transfer_file_to_list(obj.user_list)
# obj.user_list.display()
# data_transfer_list_to_file(obj.user_list)
# print(obj.user_list.is_empty())
