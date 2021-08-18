def num_translate_adv(s):
    rus_nums = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
    eng_nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    translate_dict = dict(zip(eng_nums, rus_nums))
    if s[0].istitle():
        s = s.lower()
        return translate_dict.get(s).title()
    return translate_dict.get(s)


while True:
    num = input('Введите число от 0 до 10 на английском (введите exit для выхода): ')
    print(num_translate_adv(num))
    if num == 'exit':
        break
