import json




# функция сплит в списке с операндом тк он нам понадобится
def spliter(string):
    if "+" in string:
        string = string.split("+")
        string.append("+")
    elif "*" in string:
        string = string.split("*")
        string.append("*")
    elif "^" in string:
        string = string.split("^")
        string.append("^")
    elif "|" in string:
        string = string.split("|")
        string.append("|")

    return string


# гетер списка диапазонов от значения сирАЙДИ
def getResolveFromCirID(cirID):
    rslt_lst = []
    for i in cirID:
        for j in range(len(data["items"])):
            if data["items"][j]["cirID"] == i:
                rslt_lst.append(data["items"][j]["resolve"])
    return rslt_lst


# берем элемент из json файла
def getElement():
    for i in range(len(data["items"])):
        if data["items"][i]["evaluate"] != "":
            item = spliter(data["items"][i]["evaluate"])
            if item[0] != '':
                data["items"][i]["evaluate"].pop(item)
                return item


# результат записи без форматирования нотациями
def replacer(lst):
    result_resolve = ""
    for i in lst:
        if lst.index(i) != -1:
            i = f'{i}{getElement()[-1]}'
            result_resolve += i
    return result_resolve[:-1]


# деление на списки диапазонов и их операнда
def new_digits(string):
    string = spliter(string)
    int_digits = []
    for i in string:
        i = i.split("~")
        for j in i:
            if j.isdigit():
                i = [int(j) for j in i]
        int_digits.append(i)
    return int_digits


# разбитие диапазонов на списки последовательных чисел
def counter(lst):
    first_list = []
    second_list = []
    length = len(lst)
    for i in lst[:2]:
        first_digit = i[0]
        second_digit = i[1]
        for j in range(first_digit, second_digit + 1):
            if lst.index(i) == 0:
                first_list.append(j)
            else:
                second_list.append(j)
    return first_list, second_list


# операнд * / |
def operand_unification(tuple):
    new_list = []
    for i in tuple[0]:
        if i in tuple[1]:
            new_list.append(i)
        else:
            continue
    return new_list


# операнд +
def operand_plus(tuple):
    for i in tuple[0]:
        if i in tuple[1]:
            tuple[1].remove(i)
    new_list = tuple[0] + tuple[1]
    new_list.sort()
    return new_list


# операнд ^
def operand_not(tuple):
    ALL = counter(new_digits(replacer(getResolveFromCirID(getElement()))))[0]
    for i in tuple[1]:
        if i in ALL:
            ALL.remove(i)
    ALL.sort()
    return ALL


# получаем список диапазонов!!!
def range_list(lst):
    result_list = []
    new_list = []
    for i in range(1, len(lst)):
        if lst[i] - lst[i - 1] == 1:
            if lst[i] != lst[-1]:
                new_list.append(lst[i - 1])
            else:
                new_list.append(lst[i])
                result_list.append(new_list[0])
                result_list.append(new_list[-1])
                new_list.clear()
        else:
            new_list.append(lst[i - 1])
            result_list.append(new_list[0])
            result_list.append(new_list[-1])
            new_list.clear()
    result_list.sort()
    return result_list


def stringer(lst):
    string = ""
    for i in lst:
        if lst.index(i) % 2 == 0:
            string += f'{i}~'
        elif i == lst[-1]:
            string += f'{i}'
        else:
            string += f'{i}|'
    return string


def main():
    if new_digits(replacer(getResolveFromCirID(getElement())))[-1] == ["+"]:
        return stringer(range_list(operand_plus(counter(new_digits(replacer(getResolveFromCirID(getElement())))))))
    elif new_digits(replacer(getResolveFromCirID(getElement())))[-1] == ["|"]:
        return stringer(range_list(operand_plus(counter(new_digits(replacer(getResolveFromCirID(getElement())))))))
    elif new_digits(replacer(getResolveFromCirID(getElement())))[-1] == ["*"]:
        return stringer(range_list(operand_unification(counter(new_digits(replacer(getResolveFromCirID(getElement())))))))
    elif new_digits(replacer(getResolveFromCirID(getElement())))[-1] == ["^"]:
        return stringer(range_list(operand_not(counter(new_digits(replacer(getResolveFromCirID(getElement())))))))


def json_writer():
    string = ''
    if len(getResolveFromCirID(getElement())) == 2:
        string = f'"resolve": "{main()}"'
    else:
        for i in range(len(getResolveFromCirID(getElement()))):
            pass
    return string


def evaluate_remover():
    for i in range(len(data["items"])):
        if (data["items"][i]["evaluate"]) is not None:
            main()
# print(json_writer())
# print(data["items"][7])


