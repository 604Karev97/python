for num in range(1, 101):
    if str(num)[-1] == '1':
        if str(num) == '11':
            print('%d процентов' % num)
        else:
            print('%d процент' % num)
    elif str(num)[-1] == '2' or str(num)[-1] == '3' or str(num)[-1] == '4':
        if str(num) == '12' or str(num) == '13' or str(num) == '14':
            print('%d процентов' % num)
        else:
            print('%d процентa' % num)
    else:
        print('%d процентов' % num)
