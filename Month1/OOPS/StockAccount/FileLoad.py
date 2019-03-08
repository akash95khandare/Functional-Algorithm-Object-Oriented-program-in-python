import json


def json_file_load(file_name):
    with open(file_name, 'r') as file_data:
        file_data = json.load(file_data)
        return file_data


def json_file_write(file_name, data):
    with open(file_name, 'w') as file_data:
        json.dump(data, file_data)
