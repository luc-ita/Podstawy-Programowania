matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]
matrix_c = [[5, 6, 7, 8]]


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    new_matrix = []

    for i in range(cols):
        new_matrix += [[0] * rows]

    for i in range(rows):
        for j in range(cols):
            new_matrix[j][i] = matrix[i][j]

    for i in matrix:
        print(i)
    print()
    for i in new_matrix:
        print(i)
    print()

    return

transpose(matrix_a)
transpose(matrix_b)
transpose(matrix_c)