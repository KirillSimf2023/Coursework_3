import os
from utils import *


DATA_PATH = os.path.join('data/operations.json')

def main():
    data = load_data(DATA_PATH)
    print(data)



if __name__ == '__main__':
    main()

