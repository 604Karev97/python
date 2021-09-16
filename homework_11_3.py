class OnlyNumbersError(Exception):
    pass


lst = []
while True:
    try:
        el = input('Введите данные: ')
        if not el.replace('.', '').isdigit():
            if el == 'stop':
                print(lst)
                exit()
            else:
                raise (OnlyNumbersError())
        else:
            lst.append(el)
    except OnlyNumbersError:
        print("Need only numbers!")
