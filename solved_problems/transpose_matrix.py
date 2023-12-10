from typing import List


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    rows, cols = len(matrix), len(matrix[0])

    # Creating a 2D array with transposed dimensions
    transposeM = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            value = matrix[i][j]
            transposeM[j][i] = value

    return transposeM


mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = transpose(mat)
for row in transposed_matrix:
    print(row)
