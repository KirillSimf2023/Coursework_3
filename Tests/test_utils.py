from utils import *
# from config import *


def test_load_data():
    data = load_data(os.path.join('./data/operations.json'))
    assert isinstance(data, list)
    assert load_data(os.path.join(' ')) == None


def test_format_score():
    assert format_score("Счет 90424923579946435907") == 'Счет **3590'
    assert format_score("Visa Classic 2842878893689012") == 'Visa Classic 2842 87** **** 9012'
    assert format_score("Maestro 7810846596785568") == 'Maestro 7810 84** **** 5568'

def test_formatted_data():
    assert formatted_data([{
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",
    "operationAmount": {
      "amount": "41096.24",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 90424923579946435907"}
  ]) == ['08.12.2019 Открытие вклада\n-> Счет **3590\n41096.24 USD\n']
    assert formatted_data([{
    "id": 114832369,
    "state": "EXECUTED",
    "date": "2019-12-07T06:17:14.634890",
    "operationAmount": {
      "amount": "48150.39",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Classic 2842878893689012",
    "to": "Счет 35158586384610753655"
  }
    ]) == ['07.12.2019 Перевод организации\nVisa Classic 2842 87** **** 9012 -> Счет **5365\n48150.39 USD\n']