from copy import deepcopy


class Matrix(object):
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))

    def __add__(self, other):
        result = deepcopy(self)
        if self.size() == other.size():
            for row in range(other.size()[0]):
                for col in range(other.size()[1]):
                    result.matrix[row][col] = self.matrix[row][col] + other.matrix[row][col]
            return result
        else:
            print('Разная размерность матриц. Сложение невозможно.')


if __name__ == '__main__':
    matr_A = Matrix([[2, 1, 4],
                     [5, 2, 1]])
    print('Матрица A:', matr_A, sep='\n')

    matr_N = Matrix([[2, 3],
                     [9, 8],
                     [0, -0.5]])
    print('Матрица N:', matr_N, sep='\n')

    matr_B = Matrix([[1, 2, 3],
                     [4, 5, 6]])
    print('Матрица B:', matr_B, sep='\n')

    print('Сумма матриц А и N:', matr_A + matr_N, sep='\n')
    print('Сумма матриц А и B:', matr_A + matr_B, sep='\n')
