def sep_plus_minus(s):  # функция разделения знака от числа
    return list(s)[0], s.split(list(s)[0])[1]


def get_quotations_for_num(s):  # функция расставления кавычек и перевод целого числа до 2х знаков
    return '"' + f'{int(s):02d}' + '"'


start_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in range(len(start_list)):
    if start_list[i].startswith('+') or start_list[i].startswith('-'):
        start_list[i:(i + 1)] = sep_plus_minus(start_list[i])
    if start_list[i].isdigit():
        start_list[i] = get_quotations_for_num(start_list[i])

print(start_list)
print(' '.join(start_list))
