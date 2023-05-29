import json


def read(filename):
    with open(filename, 'r', encoding="UTF-8") as file:
        return json.load(file)


data = read("new.json")


def return_values(i, item):
    return data["items"][i][item]


