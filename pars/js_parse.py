import json
from os import listdir
from os.path import isfile, join


def get_file_name(path: str):
    return [f for f in listdir(path) if isfile(join(path, f))]


def open_file (path: str, name_file: str):
    try:
        with open (file=f"{path} + {name_file}", mode="r", buffering="UTF-8") as f:
            return 
    except Exception as e:
        print(f"{e}")


def pars_js (file_name: list):
    pass


def main (path : str):
    data_file_name = get_file_name(path)
    print(data_file_name)





if __name__ == "__main__":
    path_to_first_file = "./firs_data"
    main(path_to_first_file)