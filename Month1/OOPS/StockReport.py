import json


class StockReport:
    def __init__(self):
        self.list = []

    def stock_report(self):
        with open("Json_Files/Stock.json") as data:
            data = json.loads(data)
            for i in data:
                self.list.append(i)
            print(data)


stock = StockReport()
stock.stock_report()
