import json


class DataMngRPW:
    def __init__(self):
        with open("DataMngRPW.json") as json_file:
            data = json.load(json_file)
            for i in data["rice"]:
                print(i)


obj = DataMngRPW()