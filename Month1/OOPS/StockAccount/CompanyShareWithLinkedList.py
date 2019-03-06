from OOPS.StockAccount import FileLoad
from util.LinkedList import LinkedList


class CompanyShareWithLinkedList:
    def __init__(self):
        self.customer_list = LinkedList()
        self.company_list = LinkedList()

    def add_new_customer(self):
        customer_data = FileLoad.json_file_load("Customer.json")
        for i in customer_data:
            self.customer_list.add(i)
        customer_id = input("Enter id : ")
        customer_name = input("Enter name : ").strip()
        balance = input("Enter balance to add share market account : ")
        data = {}
        new_customer = {"id": customer_id, "name": customer_name, "balance": balance, "data": data}
        flag = True
        for i in range(self.customer_list.size()):
            temp = self.customer_list.get_by_index(i)
            if temp["id"] == customer_id or str(temp["name"]).lower() == customer_name.lower():
                print("Your account already available.")
                flag = False
                break
        if flag:
            self.customer_list.add(new_customer)

        list = []
        size = self.customer_list.size()
        for i in range(size):
            list.append(self.customer_list.poll_first())

        FileLoad.json_file_write("Customer.json", list)

    def add_new_company(self):
        company_data = FileLoad.json_file_load("Company.json")
        for i in company_data:
            self.company_list.add(i)
        company_name = input("ENter company name : ")
        no_of_share = input("Enter number of share : ")
        price = input("Enter share per price : ")
        balance = input("Enter balance amount : ")
        new_company = {company_name: {"no_of_share": no_of_share, "price": price, "balance": balance}}
        flag = True
        for i in range(self.company_list.size()):
            data = self.company_list.get_by_index(i)
            if data.get(company_name) == None:
                print("Your account already available.")
                flag = False
                break
        if flag:
            self.company_list.add(new_company)

        list = []
        size = self.company_list.size()
        for i in range(size):
            list.append(self.company_list.poll_first())
        print(self.company_list.display())


if __name__ == "__main__":
    obj = CompanyShareWithLinkedList()
    obj.add_new_company()
