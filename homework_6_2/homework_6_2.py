# ------------------------------------------------------------------------#
#                             ЗАДАНИЕ 3                                   #
# ------------------------------------------------------------------------#

# from pprint import pprint
# import json
#
# dct_data = {}
#
# with open('names.txt', 'r', encoding='utf-8') as f_name, \
#         open('hobbies.txt', 'r', encoding='utf-8') as f_hobby, \
#         open('users_data.json', 'w', encoding='utf-8') as f_user_date:
#     names = f_name.read().splitlines()
#     hobbies = f_hobby.read().splitlines()
#     if len(names) > len(hobbies):
#         [hobbies.append(None) for _ in range(len(names) - len(hobbies))]
#     elif len(names) < len(hobbies):
#         exit(1)
#     for name, hobby in zip(names, hobbies):
#         dct_data[name.replace(',', '')] = hobby
#     json_dct_data = json.dumps(dct_data)
#     f_user_date.write(json_dct_data)
#
# pprint(dct_data)
#
# with open('users_data.json', 'r', encoding='utf-8') as f:
#     pprint(json.loads(f.read()))

# /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

# ------------------------------------------------------------------------#
#                             ЗАДАНИЕ 4*                                  #
# ------------------------------------------------------------------------#
# def count_lines(file_name):
#     count = 0
#     with open(file_name, 'r', encoding='utf-8') as f:
#         for _ in f:
#             count += 1
#     return count
#
#
# def append_none(file_name):
#     with open(file_name, 'a', encoding='utf-8') as f:
#         f.write(str(None))
#         f.write('\n')
#
#
# if count_lines('names.txt') > count_lines('hobbies.txt'):
#     [append_none('hobbies.txt') for _ in range(count_lines('names.txt') - count_lines('hobbies.txt'))]
# elif count_lines('names.txt') < count_lines('hobbies.txt'):
#     exit(1)
#
# with open('names.txt', 'r', encoding='utf-8') as f_name, \
#         open('hobbies.txt', 'r', encoding='utf-8') as f_hobby, \
#         open('users_hobby.txt', 'w', encoding='utf-8') as f_users_hobby:
#     for name, hobby in zip(f_name, f_hobby):
#         name = name.replace('\n', '').replace(',', '')
#         f_users_hobby.write(f'{name}: {hobby}')

# /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

# ------------------------------------------------------------------------#
#                             ЗАДАНИЕ 5*                                  #
# ------------------------------------------------------------------------#

# def count_lines(file_name):
#     count = 0
#     with open(file_name, 'r', encoding='utf-8') as f:
#         for _ in f:
#             count += 1
#     return count
#
#
# def append_none(file_name):
#     with open(file_name, 'a', encoding='utf-8') as f:
#         f.write(str(None))
#         f.write('\n')
#
#
# print('''
# Программа для обработки 2х файлов. Файлы вводятся с расширением через ".".
# Если количество строк хобби меньше, чем строк ФИО - заполняются None.
# Если количество строк ФИО меньше, чем строк хобби - выполнится выход из программы с кодом 1.
# Для выхода из программы наберите "exit" в любом из полей ввода.
# ''')
#
# while True:
#     names = input('Введите название документа ФИО: ')
#     if names == 'exit':
#         break
#     hobbies = input('Введите название документа хобби: ')
#     if names == 'exit':
#         break
#     result = input('Введите название документа записи данных: ')
#     if names == 'exit':
#         break
#     if count_lines(names) > count_lines(hobbies):
#         [append_none(hobbies) for _ in range(count_lines(names) - count_lines(hobbies))]
#     elif count_lines(names) < count_lines(hobbies):
#         print('Количество ФИО меньше, чем хобби')
#         exit(1)
#
#     with open(names, 'r', encoding='utf-8') as f_name, \
#             open(hobbies, 'r', encoding='utf-8') as f_hobby, \
#             open(result, 'w', encoding='utf-8') as f_users_hobby:
#         for name, hobby in zip(f_name, f_hobby):
#             name = name.replace('\n', '').replace(',', '')
#             f_users_hobby.write(f'{name}: {hobby}')
#     print('Документ записан!', end='\n\n')

# /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

# ------------------------------------------------------------------------#
#                             ЗАДАНИЕ 5*(со скриптом)                     #
# ------------------------------------------------------------------------#
import sys


def count_lines(file_name):
    count = 0
    with open(file_name, 'r', encoding='utf-8') as f:
        for _ in f:
            count += 1
    return count


def append_none(file_name):
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(str(None))
        f.write('\n')


names = sys.argv[1]
hobbies = sys.argv[2]
result = sys.argv[3]

if count_lines(names) > count_lines(hobbies):
    [append_none(hobbies) for _ in range(count_lines(names) - count_lines(hobbies))]
elif count_lines(names) < count_lines(hobbies):
    exit(1)

with open(names, 'r', encoding='utf-8') as f_name, \
        open(hobbies, 'r', encoding='utf-8') as f_hobby, \
        open(result, 'w', encoding='utf-8') as f_users_hobby:
    for name, hobby in zip(f_name, f_hobby):
        name = name.replace('\n', '').replace(',', '')
        f_users_hobby.write(f'{name}: {hobby}')
print('Документ записан!')
