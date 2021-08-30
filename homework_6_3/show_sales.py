from sys import argv


def make_dct():
    dct = {}

    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in enumerate(f):
            dct[line[0] + 1] = line[1].replace('\n', '')
    return dct


if __name__ == '__main__':

    dct_bakery = make_dct()

    if len(argv) == 1:
        [print(val) for val in dct_bakery.values()]
    elif len(argv) == 2:
        [print(val) for val in list(dct_bakery.values())[int(argv[1]) - 1:]]
    elif len(argv) == 3:
        [print(val) for val in list(dct_bakery.values())[int(argv[1]) - 1: int(argv[2])]]
    else:
        print('Слишком много аргументов для выполнения операции. (Максимум 2)')
