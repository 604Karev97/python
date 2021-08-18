from pprint import pprint


def thesaurus_adv(*args):
    names_dict = dict()
    for data in args:
        data = str(data).split(' ')
        if data[1][0] not in names_dict:
            names_dict[data[1][0]] = dict()
        names_dict[data[1][0]][data[0][0]] = list()
        names_dict[data[1][0]][data[0][0]].append(' '.join(data))
    return names_dict


dct = thesaurus_adv('Максим Яковенко', 'Петр Лавров', 'Ирина Резникова', 'Павел Яковлев', 'Инна Лаврентьева',
                    'Михаил Невмержицкий', 'Антон Бондарев', 'Александр Рева', 'Матвей Богушевич')
sorted_dct = sorted(dct.items(), key=lambda x: x[0])

print('-' * 10, 'Словарь фамилий и имен', '-' * 10)
pprint(dct)
print()
print('-' * 10, 'Словарь, сортированный по фамилиям', '-' * 10)
pprint(sorted_dct)
