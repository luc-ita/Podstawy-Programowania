matrix_a = [[2,3],[1,5]]
matrix_b = [[5,0,3,7,5],[9,0,9,1,2]]
matrix_c = [[2,1],[3,5],[7,4],[4,6]]

def convert(matrix):
    new_matrix = []
    for i in matrix:
        for j in i:
            new_matrix += [j]

    print(new_matrix)
    print()
    return

convert(matrix_a)
convert(matrix_b)
convert(matrix_c)