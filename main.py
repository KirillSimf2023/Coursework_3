from utils import *


DATA_PATH = os.path.join('data/operations.json')
NUMBER_OPERATION_EXECUTED = 5

def main():
    #Загружаем данные
    data = load_data(DATA_PATH)
    if data is None:
        print("Не удалось прочитать файл с данными либо он отсутствует или не верно указан путь")
    else:
        #Данные прочитаны, дальше основная работа
        data_correct = correct_data(data)
        data_last_executed = last_executed(data_correct, NUMBER_OPERATION_EXECUTED)
        data_formated = formatted_data(data_last_executed)
        for item in data_formated:
            print(item)


if __name__ == '__main__':
    main()

