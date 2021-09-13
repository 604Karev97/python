class Cell:
    def __init__(self, num_cells):
        self._num_cells = num_cells

    def __str__(self):
        return f"{'|_|' * self._num_cells} Кол-во клеток: {self._num_cells}"

    def __add__(self, other):
        return Cell(self._num_cells + other._num_cells)

    def __radd__(self, other):
        if not isinstance(other, Cell):
            return self
        return self.__add__(other)

    def __sub__(self, other):
        if self._num_cells > other._num_cells:
            return Cell(self._num_cells - other._num_cells)
        else:
            return f'Кол-во клеток в первом слагаемом меньше, чем во втором.'

    def __mul__(self, other):
        return Cell(self._num_cells * other._num_cells)

    def __floordiv__(self, other):
        return Cell(self._num_cells // other._num_cells)

    def make_order(self, n_rows):
        lst_cells = [('|_|' * n_rows) for _ in range(self._num_cells // n_rows)]
        lst_cells.append(('|_|' * (self._num_cells % n_rows)))
        return '\n'.join(lst_cells)


cells_1 = Cell(5)
cells_2 = Cell(3)
cells_3 = Cell(7)
print(cells_1)
print(cells_2)
print(cells_3)
print(cells_1 + cells_2)
print(cells_1 + cells_2 + cells_3)
print(sum([cells_1, cells_2, cells_3]))
print(cells_1 - cells_2)
print(cells_1 - cells_3)
print(cells_1 * cells_2)
print(cells_2 * cells_3)
print(cells_1 // cells_2)
print(cells_1 // cells_3)

print((cells_1 + cells_2 + cells_3).make_order(4))
