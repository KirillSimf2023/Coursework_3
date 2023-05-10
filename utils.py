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
        if 'state' in item:
            if item['state'] == "EXECUTED":
                temp_data.append(item)
    return temp_data
