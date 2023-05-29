
import json

def read(filename):
    with open(filename, 'r', encoding="UTF-8") as file:
        return json.load(file)
A = []
B = []
data = read("new.json")
for i in data["items"]:
    A.append(i["cirID"])
for i in data["items"]:
    B.append(i["resolve"])

def find_value(id):
    try:
        indexA = A.index(id)
        result = B[indexA]
        return result
    except Exception as result:
        result = 'Идентификатор не найден.'
        return result





