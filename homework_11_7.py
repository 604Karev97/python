class ComplexNum:

    def __init__(self, re, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        if self.im > 0:
            return f'{self.re} + {self.im}j'
        elif self.im == 0:
            return f'{self.re}'
        else:
            return f'{self.re} - {abs(self.im)}j'

    def __add__(self, other):
        return ComplexNum(self.re + other.re, self.im + other.im)

    def __radd__(self, other):
        if not isinstance(other, ComplexNum):
            return self
        return self.__add__(other)

    def __sub__(self, other):
        return ComplexNum(self.re - other.re, self.im - other.im)

    def __rsub__(self, other):
        if not isinstance(other, ComplexNum):
            return self
        return self.__sub__(other)

    def __mul__(self, other):
        return ComplexNum(self.re * other.re - self.im * other.im, self.re * other.im + other.re * self.im)


print(ComplexNum(5, 6))
print(ComplexNum(5, 0))
print(ComplexNum(5, -6))
print(ComplexNum(-5, -6))
print(ComplexNum(-5, -6) + ComplexNum(10, 10))
print(ComplexNum(-5, -6) - ComplexNum(10, 10))
print(ComplexNum(-5, -6) * ComplexNum(10, 10))
