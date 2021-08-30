from pprint import pprint

NAME_FILE = r'C:\Users\мвидео\Desktop\GeekBrains\nginx_logs.txt'
list_of_turples = []
dict_of_spamer = {}
count = 1

with open(NAME_FILE, 'r', encoding='utf-8') as f:
    for line in f:

        line = line.replace('\n', '').replace('\r', '').replace('"', '').split(' ')
        ID, GET, PATH = line[0], line[5], line[6]

        list_of_turples.append((ID, GET, PATH))
        if ID not in dict_of_spamer:
            dict_of_spamer[ID] = 1
        else:
            dict_of_spamer[ID] += 1

pprint(list_of_turples)
pprint(dict_of_spamer)
print(f'Максимальное число запросов - {max(dict_of_spamer.values())} раз у '
      f'ID: {list(dict_of_spamer.keys())[list(dict_of_spamer.values()).index(max(dict_of_spamer.values()))]}')
