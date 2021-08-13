def separate():
    print('-' * 60)


separate()
print('Для выхода из программы введите вместо секунд букву "x"')
separate()

while True:
    duration = input('Введите продолжительность времени в секундах: ')

    if duration == 'x' or duration == 'ч':
        break

    duration = int(duration)
    d_seconds = duration % 60
    d_minuts = (duration // 60) % 60
    d_hours = ((duration // 60) // 60) % 24
    d_days = ((duration // 24) // 60) // 60

    lst_duration = ['%d дн ' % d_days, '%d час ' % d_hours, '%d мин ' % d_minuts, '%d сек' % d_seconds]

    if d_minuts == 0 and d_hours == 0 and d_days == 0:
        print(lst_duration[-1])
        separate()
    elif d_hours == 0 and d_days == 0:
        print(lst_duration[-2] + lst_duration[-1])
        separate()
    elif d_days == 0:
        print(lst_duration[-3] + lst_duration[-2] + lst_duration[-1])
        separate()
    else:
        print(lst_duration[-4] + lst_duration[-3] + lst_duration[-2] + lst_duration[-1])
        separate()
