def summator(number):
    nums = ([el for el in str(number)])
    sum = 0
    for num in nums:
        sum += int(num)
    return sum


lst_cube = []
[lst_cube.append(num ** 3) for num in range(0, 1000) if num % 2 != 0]
print(lst_cube)

lst_sum_for_seven = []
[lst_sum_for_seven.append(num) for num in lst_cube if summator(num) % 7 == 0]
print(sum(lst_sum_for_seven))

lst_cube.clear()
[lst_cube.append(num ** 3 + 17) for num in range(0, 1000) if num % 2 != 0]
print(lst_cube)

lst_sum_for_seven.clear()
[lst_sum_for_seven.append(num) for num in lst_cube if summator(num) % 7 == 0]
print(sum(lst_sum_for_seven))
