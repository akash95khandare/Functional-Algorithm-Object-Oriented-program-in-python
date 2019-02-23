from com.bridgelab.DataStructure.Banking.GetAndStore import data_transfer_file_to_list, data_transfer_list_to_file
from com.bridgelab.util.LinkedList import LinkedList


class Casher:
    def __init__(self):
        self.user_list = LinkedList()

    def account_created(self, account_no):


    def withdraw():

    def deposit():


obj = Casher()
data_transfer_file_to_list(obj.user_list)
obj.user_list.display()
data_transfer_list_to_file(obj.user_list)
print(obj.user_list.is_empty())
