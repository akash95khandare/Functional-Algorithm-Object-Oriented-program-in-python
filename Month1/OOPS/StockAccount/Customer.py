from OOPS.StockAccount import FileLoad


class Customer:
    def __init__(self):
        self.company_data = FileLoad.json_file_load("Company.json")
        self.customer_data = FileLoad.json_file_load("Customer.json")
        self.cus_index = 0

    def buy(self, customer_id, company_name, customer_name, no_of_share):
        cus_index = 0
        for i in range(len(self.customer_data)):
            if int(self.customer_data[i]["id"]) == customer_id and str(
                    self.customer_data[i]["name"]).lower() == customer_name.lower():
                cus_index = i
                self.cus_index = i
        total_amount = no_of_share * int(self.company_data[company_name]["price"])
        if int(self.customer_data[cus_index].get("balance")) >= total_amount and int(
                self.company_data[company_name].get("no_of_share")) >= no_of_share:
            self.customer_data[cus_index]["balance"] = str(int(self.customer_data[cus_index].get("balance")) - total_amount)
            self.customer_data[cus_index]["data"][company_name] = str(int(self.customer_data[cus_index]["data"].get(company_name)) + no_of_share)
            # print(self.company_data[company_name].get("no_of_share"))
            self.company_data[company_name]["no_of_share"] = str(int(self.company_data[company_name].get("no_of_share")) - no_of_share)
            self.company_data[company_name]["balance"] = str(int(self.company_data[company_name]["balance"]) + total_amount)

    def sell(self, customer_id, company_name, customer_name, no_of_share):
        cus_index = 0
        for i in range(len(self.customer_data)):
            if int(self.customer_data[i]["id"]) == customer_id and str(
                    self.customer_data[i]["name"]).lower() == customer_name.lower():
                cus_index = i
                self.cus_index = i
        total_amount = no_of_share * int(self.company_data[company_name]["price"])

        if int(self.company_data[company_name].get("balance")) >= total_amount and int(
                self.customer_data[cus_index]["data"].get(company_name)) >= no_of_share:
            self.customer_data[cus_index]["balance"] = str(int(self.customer_data[cus_index].get("balance")) + total_amount)
            self.customer_data[cus_index]["data"][company_name] = str(int(
                self.customer_data[cus_index]["data"].get(company_name)) - no_of_share)
            # print(self.company_data[company_name].get("no_of_share"))
            self.company_data[company_name]["no_of_share"] = str(int(
                self.company_data[company_name].get("no_of_share")) + no_of_share)
            self.company_data[company_name]["balance"] = str(int(self.company_data[company_name]["balance"]) - total_amount)

    def save(self):
        if self.company_data == None or self.customer_data == None:
            print("Data is not read")
            return
        FileLoad.json_file_write("Customer.json", self.customer_data)
        FileLoad.json_file_write("Company.json", self.company_data)

    def print_report(self):
        print(self.customer_data[self.cus_index])


obj = Customer()
# obj.buy(1234, "Google", "Akash", 10)
obj.sell(1234, "Google", "Akash", 10)
obj.save()
