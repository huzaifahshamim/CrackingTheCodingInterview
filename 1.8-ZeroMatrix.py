"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
"""


def ZeroMatrix(matrix):
    row_zeros = []
    col_zeros = []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == 0:
                row_zeros.append(row)
                col_zeros.append(column)

    #print(row_zeros)
    for rowval in row_zeros:
        #print(rowval)
        for val in range(len(matrix[rowval])):
            #print(val)
            matrix[rowval][val] = 0

    print(col_zeros)
    for colval in col_zeros:
        #print(colval)
        for val2 in range(len(matrix)):
            #print(val2)
            matrix[val2][colval] = 0

    return matrix


matrix1 = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]
ans1 = ZeroMatrix(matrix1)
print(ans1)

matrix2 = [[0, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]
ans2 = ZeroMatrix(matrix2)
print(ans2)

matrix3 = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 0, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]
ans3 = ZeroMatrix(matrix3)
print(ans3)

matrix4 = [[1, 2, 3, 4, 0],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [0, 22, 23, 24, 25]]
ans4 = ZeroMatrix(matrix4)
print(ans4)

