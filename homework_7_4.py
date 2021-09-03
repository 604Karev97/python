import os
import json

dct_sizes = {}
root_dir = f'{input("Введите название директории: ")}/'
json_name = f'{root_dir.replace("/", "")}_summary.json'
# root_dir = './'

lst_of_100 = []
lst_of_1000 = []
lst_of_10000 = []
lst_of_100000 = []
lst_of_biggest = []

for root, dirs, files in os.walk(root_dir):
    for file in files:
        f_path = os.path.join(root, file)
        if os.stat(f_path).st_size >= 0 and os.stat(f_path).st_size <= 100:
            lst_of_100.append(file.split('.')[-1])
        elif os.stat(f_path).st_size > 100 and os.stat(f_path).st_size <= 1000:
            lst_of_1000.append(file.split('.')[-1])
        elif os.stat(f_path).st_size > 1000 and os.stat(f_path).st_size <= 10000:
            lst_of_10000.append(file.split('.')[-1])
        elif os.stat(f_path).st_size > 10000 and os.stat(f_path).st_size <= 100000:
            lst_of_100000.append(file.split('.')[-1])
        else:
            lst_of_biggest.append(file.split('.')[-1])

dct_sizes[100] = (len(lst_of_100), list(set([el for el in lst_of_100])))
dct_sizes[1000] = (len(lst_of_1000), list(set([el for el in lst_of_1000])))
dct_sizes[10000] = (len(lst_of_10000), list(set([el for el in lst_of_10000])))
dct_sizes[100000] = (len(lst_of_100000), list(set([el for el in lst_of_100000])))
dct_sizes['biggest'] = (len(lst_of_biggest), list(set([el for el in lst_of_biggest])))

with open(os.path.join(root_dir, json_name), 'w', encoding='utf-8') as f:
    json.dump(dct_sizes, f)
