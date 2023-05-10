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

