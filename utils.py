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
        date = f'{item["date"][8:10]}.{item["date"][5:7]}.{item["date"][:4]}'
        str1 = date + ' ' + item["description"]

        if 'from' in item:
            sender = item["from"]
            recipient = item["to"]
            str2 = f"{format_score(sender)} -> {format_score(recipient)}"
        else:
            recipient = item["to"]
            str2 = f"-> {format_score(recipient)}"
        str3 = item["operationAmount"]["amount"] + ' ' + item["operationAmount"]["currency"]["name"]
        return_data.append(f"""\
{str1}
{str2}
{str3}
""")
    return return_data


def format_score(score_str: str) -> str:
    temp_str = score_str.split()
    if temp_str[0] == 'Счет':
        return f'{temp_str[0]} **{temp_str[1][-5:-1]}'
    else:
        if len(temp_str) == 2:
            return f'{temp_str[0]} {temp_str[1][:4]} {temp_str[1][4:6]}** **** {temp_str[1][12:16]}'
        if len(temp_str) == 3:
            return f'{temp_str[0]} {temp_str[1]} {temp_str[2][:4]} {temp_str[2][4:6]}** **** {temp_str[2][12:16]}'



