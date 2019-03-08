import json


class StockReport:
    def __init__(self):
        self.list = []

    def new_data(self):
        dt = {"name": "",
              "no_of_share": "",
              "price": ""}
        try:
            name = input("Enter comapany name : ").strip().upper()
            no_of_share = input("Enter no of share : ").strip()
            price = input("Enter share price : ").strip()
            if not name.isalpha() or not no_of_share.isnumeric() or not price.isnumeric():
                raise ValueError
        except:
            print("You have entered wrong data.")
        else:
            dt["name"] = name
            dt["no_of_share"] = no_of_share
            dt["price"] = price
            return dt

    def stock_report(self):
        with open("Json_Files/Stock.json", 'r') as data:
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
