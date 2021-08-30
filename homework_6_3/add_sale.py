from sys import argv


def add_sale():
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(argv[1])
        f.write('\n')


if __name__ == '__main__':
    add_sale()
