import os
from sys import argv

ROOT = os.path.dirname(__file__)


def make_dirs(lst_names):
    lst_paths = [os.path.join(ROOT, f'my_project/{dr}') for dr in lst_names]
    for paths in lst_paths:
        if not os.path.exists(paths):
            os.makedirs(paths)
            msg = f'Папка {os.path.split(paths)[1]} создана.'
        else:
            msg = f'Папка {os.path.split(paths)[1]} уже существует.'
        print(msg)


def change_name_dir(last_name, new_name):
    os.rename((os.path.join(ROOT, f'my_project/{last_name}')), (os.path.join(ROOT, f'my_project/{new_name}')))


if __name__ == '__main__':
    lst_dir = ['settings', 'mainapp', 'adminapp', 'authapp']
    if len(argv) == 1:
        make_dirs(lst_dir)
    elif len(argv) == 3 and argv[2] == 'info':
        print(argv[1], os.stat(f'my_project/{argv[1]}'))
    elif len(argv) == 3:
        try:
            change_name_dir(argv[1], argv[2])
        except FileNotFoundError:
            print('Такой папки не существует.')
    else:
        print('Параметры не введены.')
