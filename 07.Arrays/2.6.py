matrix = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            matrix[i][j] = 1
        print(matrix[i][j], end=' ')
    print()