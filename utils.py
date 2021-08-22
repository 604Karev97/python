from requests import get
from decimal import Decimal
import datetime


def currency_rates(char_code):
    char_code = char_code.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)

    lst_values = []
    lst_char_codes = []
    [lst_values.append(float(Decimal(el.split('</Value>')[0].replace(',', '.')))) for el in
     content.split('<Value>')[1:]]
    [lst_char_codes.append(el.split('</CharCode>')[0]) for el in content.split('<CharCode>')[1:]]

    dct_valutes = dict(zip(lst_char_codes, lst_values))

    date = datetime.datetime.strptime(content.split('Date=')[1].split(' ')[0].replace('"', ''), '%d.%m.%Y')
    date = date.strftime('%d.%m.%Y')

    str_print = f'По состоянию {date} курс валюты {char_code} составляет {dct_valutes[char_code]} рублей.'

    return str_print if char_code in lst_char_codes else None


if __name__ == '__main__':
    while True:
        char_code = input('Введите код валюты на английском (введите exit для выхода): ')
        print(currency_rates(char_code))
        if char_code == 'exit':
            break
