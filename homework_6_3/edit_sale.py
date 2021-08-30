from sys import argv
from show_sales import make_dct


def change_value(num_pos, new_value):
    dct_bakery = make_dct()
    if int(num_pos) in dct_bakery.keys():
        dct_bakery[int(num_pos)] = new_value
        with open('bakery.csv', 'w', encoding='utf-8') as f:
            [f.write(val) and f.write('\n') for val in dct_bakery.values()]
    else:
        print('Такой позиции нет в документе.', end='\n')


if __name__ == '__main__':
    change_value(argv[1], argv[2])
