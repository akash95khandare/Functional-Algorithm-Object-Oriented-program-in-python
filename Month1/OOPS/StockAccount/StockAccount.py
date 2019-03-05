from OOPS.StockAccount.Customer import Customer


class StockAccount:
    def __init__(self):
        self.customer = Customer()

    def stock_account(self):
        while True:
            print("------Share Stock Account--------\n1.Buy\n2.Sell\n3Save\n4Print Report")
            choice = input("Select any one : ")
            if choice == 1 or choice == 2:
                customer_id = int(input("Enter id : "))
                customer_name = input("Enter name : ")
                company_name = input("Enter company name : ")
                no_of_share = int(input("Enter number of share : "))
            service = [self.customer.buy(customer_id, company_name, customer_name, no_of_share),
                       self.customer.sell(customer_id, company_name, customer_name, no_of_share),
                       self.customer.save(),
                       self.customer.print_report()]
            service[choice]

if __name__ == "__main__":
    stock_account = StockAccount()
    stock_account.stock_account()