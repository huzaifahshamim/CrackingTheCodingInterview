"""
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""

def RotateMatrix(matrix):
    n = len(matrix)
    for layer in range(n):
        for cell in range(n):
            tl = matrix[layer][cell + layer]
            tr = matrix[cell + layer][n-1 - layer]
            br = matrix[n-1 - layer][n-1 - cell - layer]
            bl = matrix[n-1 - cell - layer][cell + layer]

            matrix[layer][cell + layer] = bl
            matrix[cell + layer][n - 1 - layer] = tl
            matrix[n - 1 - layer][n - 1 - cell - layer] = tr
            matrix[n - 1 - cell - layer][cell + layer] = br
    return matrix