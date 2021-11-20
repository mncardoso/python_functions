# Matrix Calculations

def element(matrix: list, line: int, column: int):
    '''matrix element

    [[1, 2, 3],
     [4, 5, 6]]

    '''

    if len(matrix) > (line + 1):
        matrix_line = matrix[line]
        if len(matrix_line) > (column + 1):
            return matrix_line[column]

        else:
            raise ValueError("matrix_element: invalid index, column", column)

    else:
        raise ValueError("matrix_element: invalid index, line", l)


def print(matrix: list):
    '''matrix_print

    '''

    for line in matrix:
        print(line)


def sum(matrix1: list, matrix2: list):
    '''matrix_sum

    '''

    line = 0
    matrix_sum = []

    while line < len(matrix1):
        matrix_sum.append([])
        matrix1_line = matrix1[line]
        matrix2_line = matrix2[line]
        element = 0

        while element < len(m1_s):
            matrix_sum[line].append(
                matrix1_line[element] + matrix2_line[element])
            element += 1
        line += 1

    return matrix_sum


def mult(matrix1: list, matrix2: list):
    '''matrix_mult

    '''

    matrix_mult = []
    line_index = 0

    for line in range(len(matrix1)):
        matrix_mult_line = []
        for column in range(len(matrix2[line_index])):
            mult = 0
            for element in range(len(matrix2)):
                mult += matrix1[line][element] * matrix2[element][column]
            matrix_mult_line.append(mult)
        matrix_mult.append(matrix_mult_line)
    line_index += 1

    return matrix_mult
