"""
Overview : Stock Report
purpose : writing new json data into json file
class name : StockReport
author : Akash Khandare
date : 05/03/2019
"""
import json


class StockReport:
    def __init__(self):
        self.list = []
        with open("Json_Files/Stock.json", 'r') as data:
            try:
                data = json.load(data)
                for i in data:
                    self.list.append(i)
            except Exception:
                print("File is empty.")

    def new_data(self):
        """
        Taking new data from user and make json data
        :return: return dt as new created json data
        """
        dt = {"name": "",
              "no_of_share": "",
              "price": ""}
        try:
            name = input("Enter company name : ").strip().upper()
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
        """
        reading old data from json file in list and
        add new json data into list and then write list into json file
        :return:
        """

        dt = self.new_data()
        self.list.append(dt)
        # print(self.list)

        with open("Json_Files/Stock.json", 'w') as da:
            json.dump(self.list, da)
            print("Company Added.")

    def display(self):
        print("Company name\t\tNo of share\t\tPer share price")
        for i in self.list:
            print(i["name"], "\t\t\t\t", i["no_of_share"], "\t\t\t\t", i["price"])


# Main method
if __name__ == "__main__":
    stock = StockReport()
    stock.display()
    stock.stock_report()
    stock.display()
