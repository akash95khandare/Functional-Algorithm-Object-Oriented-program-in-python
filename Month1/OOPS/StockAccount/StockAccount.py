from OOPS.StockAccount.CompanyShareWithLinkedList import CompanyShareWithLinkedList
from OOPS.StockAccount.Customer import Customer


class StockAccount:
    def __init__(self):
        self.customer = Customer()
        self.new_data_add = CompanyShareWithLinkedList()

    def stock_account(self):
        while True:
            print(
                "------Share Stock Account--------\n1.Add Customer\n2.Add Company\n"+
                "3.Buy\n4.Sell\n5.Save\n6.Print Report\n7.Exit")
            choice = int(input("Select any one : "))
            if choice == 3 or choice == 4:
                try:
                    customer_id = int(input("Enter customer id : "))
                    customer_name = input("Enter customer name : ").strip().upper()
                    company_name = input("Enter company name : ").strip().upper()
                    no_of_share = int(input("Enter number of share : "))
                    if not customer_name.isalpha() or not company_name.isalpha():
                        raise ValueError
                except ValueError:
                    print("You have entered wrong data.")
                    continue
            service = {1: "add_new_customer", 2: "add_new_company", 3: "buy", 4: "sell", 5: "save", 6: "print_report"}
            if choice == 7:
                break
            if choice == 1 or 2:
                fun = getattr(self.new_data_add, service[choice])
            else:
                fun = getattr(self.customer, service[choice])
            if choice == 3 or choice == 4:
                fun(customer_id, company_name, customer_name, no_of_share)
            else:
                fun()


if __name__ == "__main__":
    stock_account = StockAccount()
    stock_account.stock_account()
