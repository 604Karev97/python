from functools import wraps


def type_logger(callback):
    @wraps(callback)
    def wrapper(*args):
        area = callback(*args)
        dct = {}
        for arg in args:
            dct[arg] = type(arg)
        print(callback.__name__, dct, type(area))
        return area

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


@type_logger
def calc_mult(a, b, c):
    return a * b * c


@type_logger
def calc_separation(a, b, c):
    return a / b / c


print(calc_cube(3))
print(calc_mult(10, 55.555, 1 / 4))
print(calc_separation(5, 1, 6))
