from utils import *
# from config import *


def test_load_data():
    data = load_data(os.path.join('operations.json'))
    assert isinstance(data, list)
    assert load_data(os.path.join(' ')) == None

