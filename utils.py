import json
import os.path

def load_data(path):
    """
    Загружает данные из файла json
    :param path: путь к файлу json
    :return: list словарей с даннфми
    """
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def correct_data(data: list) -> list:
    """
    Фильтруем данные, оставляем только те у которых поле state = "EXECUTED"
    :param data: list словарей с данными
    :return: отфильтрованный list словарей
    """
    temp_data = []
    for item in data:
        if 'state' in item and item['state'] == "EXECUTED":
            temp_data.append(item)
    return temp_data

def last_executed(data: list, number: int) -> list:
    """
    Оставляем только последние операции в количестве number, в порядке убывания по дате
    :param data: отфильтрованные данные
    :param number: количество последних операций
    :return: list словарей с последними операциями
    """
    data.sort(key=lambda element: element["date"], reverse=True)
    temp_data = data[:number]
    return temp_data

def formatted_data(data: list) -> list:
    """
    Превращаем данные в читабельный формат согласно ТЗ
    :param data: list словарей с последними операциями
    :return: list стрингов
    """
    return_data=[]
    for item in data:
        date = f'{item["date"][8:10]}.{item["date"][5:7]}.{item["date"][:4]}'
        str1 = f'{date} {item["description"]}'

        if 'from' in item:
            sender = item["from"]
            recipient = item["to"]
            str2 = f"{format_score(sender)} -> {format_score(recipient)}"
        else:
            recipient = item["to"]
            str2 = f"-> {format_score(recipient)}"
        str3 = f'{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}'
        return_data.append(f"""\
{str1}
{str2}
{str3}
""")
    return return_data


def format_score(score_str: str) -> str:
    """
    Получаем стринг и форматируем его в нужном формате
    Счет 90424923579946435907 -> Счет **3590
    Maestro 7810846596785568 -> Maestro 7810 84** **** 5568
    Visa Classic 2842878893689012 -> Visa Classic 2842 87** **** 9012
    :param score_str: стринг
    :return: отформатированный стринг
    """
    temp_str = score_str.split()
    if temp_str[0] == 'Счет':
        return f'{temp_str[0]} **{temp_str[1][-5:-1]}'
    else:
        if len(temp_str) == 2:
            return f'{temp_str[0]} {temp_str[1][:4]} {temp_str[1][4:6]}** **** {temp_str[1][12:16]}'
        if len(temp_str) == 3:
            return f'{temp_str[0]} {temp_str[1]} {temp_str[2][:4]} {temp_str[2][4:6]}** **** {temp_str[2][12:16]}'



