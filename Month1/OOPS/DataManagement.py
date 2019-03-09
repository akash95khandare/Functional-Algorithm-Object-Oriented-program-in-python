"""
Overview : JSON Inventory Data Management of Rice, Pulses and Wheats.
purpose: Json Concept,reading json data and print
class name : DataManagement
author : Akash Khandare
date : 04/03/2019

"""
import json


class DataManagement:
    def __init__(self):
        """
        Loading data from json file and calculate all data
        print price and weight of inventory
        """
        price1 = weight1 = 0
        with open("Json_Files/DataMngRPW.json") as json_file:
            data = json.load(json_file)
            for i in data:
                print("***********", i, "*************")
                for j in data[i]:
                    price1 += int(j["price"])
                    weight1 += int(j["weight"])
                print("Price : ", price1)
                print("Weight : ", weight1)


"""
Main method
"""
if __name__ == '__main__':
    obj = DataManagement()
