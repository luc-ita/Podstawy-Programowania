def matrix(x):
    array  = [[0 for i in range(x)] for j in range(x)]
    for z in range(0, x):
        array[z][z] = 1
    return array

def printer(x):
    for i in matrix(x):
        print(i)
    print()

printer(3)
printer(5)
printer(8)
