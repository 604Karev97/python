def odd_nums_gen(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


print(*odd_nums_gen(15))
