import json
import os.path


def load_data(path):
    # Загружаем данные из файла
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def correct_data(data: list) -> list:
    temp_data = []
    for item in data:
        if 'state' in item and item['state'] == "EXECUTED":
            temp_data.append(item)
    return temp_data

def last_executed(data: list, number) -> list:
    #1- отсортировать по дате
    #2 - вернуть последние элементы по количеству number
    data.sort(key=lambda element: element["date"], reverse=True)
    temp_data = data[:number]
    return temp_data

def formatted_data(data: list) -> list:
    return_data=[]
    for item in data:
        str1 = item["date"] + ' ' + item["description"]

        if 'from' in item:
            # str2 = " " + ' -> ' + str(item["to"]).split()[0] + ' ' + str(item["to"]).split()[1]
            sender = item['to']
            str2 = f" -> {format_score(sender)}"
        else:
            str2 = ' -> ' + ''
        str3 = item["operationAmount"]["amount"] + ' ' + item["operationAmount"]["currency"]["name"]
        print(str1)
        print(str2)
        print(str3)
        print(' ')


    return return_data


def format_score(score_str: str) -> str:
    temp_str = score_str.split()
    if temp_str[0] == 'Счет':
        return f'{temp_str[0]} **{temp_str[1][-5:-1]}'
    else:
        return f'{temp_str[0]} {temp_str[1][:4]} {temp_str[1][4:6]}** **** {temp_str[1][12:16]}'



