"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
"""


def ZeroMatrix(matrix):
    row_zeros = []
    col_zeros = []
    for row in range(len(matrix)):
        for column in range(len(row)):
            if matrix[row][column] == 0:
                row_zeros.append(row)
                col_zeros.append(column)

    for rowval in row_zeros:
        for val in matrix[row_zeros]:
            matrix[rowval][val] = 0

    for colval in col_zeros:
        for val2 in range(len(matrix)):
            matrix[val2][colval] == 0

    return matrix
