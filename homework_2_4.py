import random


def convert_price(lst):
    for i in range(len(lst)):
        num = f'{float(lst[i]):.02f}'.split('.')
        lst[i] = f'{int(num[0]):02d} руб {num[1]} коп'
    return lst


price_list = []
nums_list = []
[price_list.append(str(round(random.uniform(1, 200), 2))) for i in range(0, 20)]
print(price_list)
[nums_list.append(float(item)) for item in price_list]
new_num_list = sorted(nums_list, reverse=True)

print(', '.join(convert_price(price_list)))
print()

print('ИД обычного списка: ', id(nums_list))
nums_list.sort()
print('ИД сортированного списка: ', id(nums_list))
print(', '.join(convert_price(nums_list)))
print()

print(', '.join(convert_price(new_num_list)))
print()

print([new_num_list[i] for i in range(5)])
