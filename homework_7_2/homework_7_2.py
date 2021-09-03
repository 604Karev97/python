import yaml
from yaml.loader import SafeLoader
import os

try:
    with open('config.yaml', 'r', encoding='utf-8') as f_yaml:
        yaml_dct = yaml.load(f_yaml, Loader=SafeLoader)

        try:

            for first_lvl in yaml_dct.items():
                if not os.path.exists(first_lvl[0]):
                    os.mkdir(first_lvl[0])

                for second_lvl in first_lvl[1].items():
                    if not os.path.exists(second_lvl[0]):
                        os.mkdir(os.path.join(first_lvl[0], second_lvl[0]))

                    for third_lvl in second_lvl[1]:
                        if type(third_lvl) == str and (third_lvl.endswith('.py') or third_lvl.endswith('.html')):
                            open(f'{os.path.join(first_lvl[0], second_lvl[0], third_lvl)}', 'w', encoding='utf-8')
                        if type(third_lvl) == dict:

                            for fourth_lvl in third_lvl.items():
                                if not os.path.exists(fourth_lvl[0]):
                                    os.mkdir(os.path.join(first_lvl[0], second_lvl[0], fourth_lvl[0]))

                                for fifth_lvl in fourth_lvl[1]:
                                    if type(fifth_lvl) == dict:

                                        for sixth_lvl in fifth_lvl.items():
                                            if not os.path.exists(sixth_lvl[0]):
                                                os.mkdir(os.path.join(first_lvl[0], second_lvl[0], fourth_lvl[0],
                                                                      sixth_lvl[0]))

                                            for seventh_lvl in sixth_lvl[1]:
                                                if type(seventh_lvl) == str and (
                                                        seventh_lvl.endswith('.py') or seventh_lvl.endswith('.html')):
                                                    open(
                                                        f'{os.path.join(first_lvl[0], second_lvl[0], fourth_lvl[0], sixth_lvl[0], seventh_lvl)}',
                                                        'w',
                                                        encoding='utf-8')

        except FileExistsError:
            print('Такие папки уже существуют')
except FileNotFoundError:
    print('Такой файл не удалось найти.')
