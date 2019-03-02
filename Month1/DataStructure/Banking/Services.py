from DataStructure.Banking import GetAndStore
from DataStructure.Banking import Customer
from util.LinkedList import LinkedList


class Services:
    def __init__(self):
        self.user_list = LinkedList()
        GetAndStore.data_transfer_file_to_list(self.user_list)

    def account_created(self):
        account_no = int(input("Enter account number : "))
        customer_name = input("Enter customer name : ")
        obj = Customer()
        obj.set_amount(00)
        obj.set_customer_name(customer_name)
        obj.set_account_no(account_no)
        self.user_list.add(obj)

    def get_data(self, account_no):
        head = self.user_list.get_head()
        while hash(head.object.get_account_no()) != hash(account_no):
            head = head.next
            if head == None:
                return -1
        return head.object

    def withdraw(self, account_no, amount, name):
        obj = self.get_data(account_no)
        if obj == -1:
            print(name, "Your account not created. First you should be create your account. ")
            print("Enter detail for account creation.")
            self.account_created()
            return
        if int(obj.get_amount()) > amount:
            obj.set_amount(str(int(obj.get_amount()) - amount))
        else:
            print("Insufficient balance.")

    def deposit(self, account_no, amount, name):
        obj = self.get_data(account_no)
        if obj == -1:
            print(name, "Your account not created. First you should be create your account. ")
            print("Enter detail for account creation.")
            self.account_created()
            return
        obj.set_amount(str(int(obj.get_amount()) + amount))

    def write(self):
        GetAndStore.data_transfer_list_to_file(self.user_list)
