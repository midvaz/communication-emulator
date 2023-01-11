
import json
from os import listdir
from os.path import isfile, join

from errors.error import write_errors_in_file as w_err

path_to_first_file = "../firs_data"

def get_file_name(path: str):
    return [f for f in listdir(path) if isfile(join(path, f))]


def open_file (path: str, name_file: str):
    try:
        with open (file=f"{path}/{name_file}", mode="r", buffering="UTF-8") as f:
            return f
    except Exception as e:
        w_err(e)
        print(f"{e}")


def pars_js (file_name: list):
    pass


def main (path : str):
    data_file_name = get_file_name(path)
    print(data_file_name)





if __name__ == "__main__":
    main(path_to_first_file)