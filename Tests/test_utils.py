from utils import *
import pytest

list_data_comparison = [{
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
    "to": "Счет 90424923579946435907"},
    {
        "id": 550607912,
        "state": "EXECUTED",
        "date": "2018-07-31T12:25:32.579413",
        "operationAmount": {
            "amount": "34380.08",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 8532498887072395",
        "to": "Счет 44238164562083919420"
    }]


@pytest.fixture
def begin_data():
    return [{
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
        "to": "Счет 90424923579946435907"},
        {
            "id": 176798279,
            "state": "CANCELED",
            "date": "2017-04-18T11:22:18.800453",
            "operationAmount": {
                "amount": "73778.48",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 90417871337969064865"
        },
        {
            "id": 550607912,
            "state": "EXECUTED",
            "date": "2018-07-31T12:25:32.579413",
            "operationAmount": {
                "amount": "34380.08",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 8532498887072395",
            "to": "Счет 44238164562083919420"
        },
        {
            "id": 560813069,
            "state": "CANCELED",
            "date": "2016-12-03T04:27:03.427014",
            "operationAmount": {
                "amount": "17628.50",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "MasterCard 1796816785869527",
            "to": "Visa Classic 7699855375169288"
        }
    ]


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


def test_correct_data(begin_data):
    assert correct_data(data=begin_data) == list_data_comparison

def test_last_executed(begin_data):
    assert last_executed(data=begin_data, number=2) == list_data_comparison
