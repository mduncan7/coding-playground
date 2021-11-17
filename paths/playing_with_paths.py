"""
Just for fun, check if file exits:
    Read it in and print the number of lines if it does. Print an error if it doesn't.
"""
import os
import pathlib

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def do_things_with_os():
    _my_file_path = os.path.abspath(os.path.join(BASE_DIR, '../data/simple.json'))
    print(dir(_my_file_path))

    if os.path.isfile(_my_file_path):
        with open(_my_file_path) as f:
            file_len = len(f.readlines())
        print(f"{file_len} lines in \"{_my_file_path}\".")
    else:
        print(f"Oops, no file at \"{_my_file_path}\".")


def do_things_with_pathlib():
    _my_file_path = pathlib.Path(BASE_DIR).joinpath("../data/simple.json")
    _my_file_path.absolute()
    print(dir(_my_file_path))
    if _my_file_path.is_file():
        with _my_file_path.open() as f:
            file_len = len(f.readlines())
        print(f"{file_len} lines in \"{_my_file_path}\".")
    else:
        print(f"Oops, no file at \"{_my_file_path}\".")


if __name__ == '__main__':
    do_things_with_os()
    # do_things_with_pathlib()
