import json


class StockReport:
    def __init__(self):
        self.list = []

    def new_data(self):
        dt = {"name": "",
              "no_of_share": "",
              "price": ""}
        name = input("Enter comapany name : ")
        no_of_share = input("Enter no of share : ")
        price = input("Enter share price : ")
        dt["name"] = name
        dt["no_of_share"] = no_of_share
        dt["price"] = price
        return dt

    def stock_report(self):
        with open("Json_Files/Company.json", 'r') as data:
            data = json.load(data)
            for i in data:
                self.list.append(i)
            dt = self.new_data()
            self.list.append(dt)
            # print(self.list)
        with open("Json_Files/Stock.json", 'w') as da:
            json.dump(self.list, da)


stock = StockReport()
stock.stock_report()
