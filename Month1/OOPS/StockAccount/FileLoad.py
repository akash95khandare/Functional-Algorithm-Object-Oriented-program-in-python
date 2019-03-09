"""
Overview : Two method for reading json data from and writing json data to json file
purpose : Reading and writing json data
author : Akash Khandare
date : 05/03/2019

"""

import json


def json_file_load(file_name):
    """
    reading json data from json file
    :param file_name: it is json file name
    :return: return json data
    """
    with open(file_name, 'r') as file_data:
        file_data = json.load(file_data)
        return file_data


def json_file_write(file_name, data):
    """
    writing json data to json file
    :param file_name: it is json file name
    :param data: it is list as json data
    """
    with open(file_name, 'w') as file_data:
        json.dump(data, file_data)


# Main method
if __name__ == "__main__":
    pass
