class NotDivisionZeroError(Exception):
    pass


try:
    num = float(input('Введите делитель: '))
    print(1/num)

except (ValueError, NotDivisionZeroError) as error:
    print(error)

except (ZeroDivisionError, NotDivisionZeroError) as error:
    print(error)
