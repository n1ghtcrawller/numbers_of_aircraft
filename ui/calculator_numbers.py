import json
import calc


def read(filename):
    with open(filename, 'r', encoding="UTF-8") as file:
        return json.load(file)


data = read("objects_file.json")


result_list = []


def getNumbersByValue():
    global result_list
    global int_list
    new_json = {"items": []}
    for i in data["items"]:
        new_list = []
        if i["evaluate"] != "":
            result = getIndexByEval(calc.spliter(i["evaluate"]))
            for j in result:
                new_list.append(data["items"][j]["resolve"])
            result_list.append(new_list)
            # i["evaluate"] = ""
            for index in range(len(result_list)):
                i["resolve"] = returner(index)

        new_json["items"].append(i)
        write_json("new.json", new_json)
    print("2.OK")

def getIndexByEval(Eval):
    lst_index = []
    list_of_cir_id = [i["cirID"] for i in data["items"]]
    for el in Eval:
        if el in list_of_cir_id:
            lst_index.append(list_of_cir_id.index(el))
        else:
            continue
    return lst_index


def split_the_list(lst):
    new_list = []
    for i in lst:
        new_list.append(i.split("~"))
    return counter(new_list)


def counter(lst):
    int_lst = []
    for i in lst:
        int_lst.append((unpacker(i)))
    return del_sames(rewriter(int_lst))


def rewriter(lst):
    length = len(lst)
    new_list = []
    for i in range(length):
        for j in range(len(lst[i])):
            new_list.append(lst[i][j])
            new_list.sort()

    return new_list


def unpacker(list):
    a = list[0]
    b = list[1]
    new_list = []
    for i in range(int(b)-int(a)):
        new_list.append(int(list[0])+i)
    new_list.append(int(list[1]))
    return new_list


def stringer(lst):
    string = ""
    for i in lst:
        if lst.index(i) % 2 == 0:
            string += f'{i}~'
        elif i == lst[-1]:
            string += f'{i}'
        else:
            string += f'{i}+'
    return string


def del_sames(lst):
    temp = []
    for i in lst:
        if i not in temp:
            temp.append(i)
    return calc.stringer(calc.range_list(temp))


def returner(index):
    return split_the_list(result_list[index])


def write_json(filename, datas):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(datas, file, indent=2)
    file.close()


getNumbersByValue()

