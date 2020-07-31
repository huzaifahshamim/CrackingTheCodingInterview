"""
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""


def RotateMatrix(matrix):
    n = len(matrix)
    for layer in range(n):
        print("THIS IS LAYER", layer)
        for cell in range(layer, n-1 -layer):
            tl = matrix[layer][cell + layer]
            print(tl)
            tr = matrix[cell + layer][n - 1 - layer]
            print(tr)
            br = matrix[n - 1 - layer][n - 1 - cell - layer]
            print(br)
            bl = matrix[n - 1 - cell - layer][layer]
            print(bl)

            matrix[layer][cell + layer] = bl
            print(matrix)
            matrix[cell + layer][n - 1 - layer] = tl
            print(matrix)
            matrix[n - 1 - layer][n - 1 - cell - layer] = tr
            print(matrix)
            matrix[n - 1 - cell - layer][layer] = br
            print(matrix)
    return matrix


"""
Space Complexity
"""

matrix1 = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]
ans1 = RotateMatrix(matrix1)
print(ans1)

'''ans2 = RotateMatrix('abcdefghhgfedcba')
print(ans2)

ans3 = RotateMatrix('asasss')
print(ans3)

ans4 = RotateMatrix('bccabe')
print(ans4)
'''