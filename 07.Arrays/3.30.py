array = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
x = 0
for i in array:
    x += 1
    y = 0
    for j in i:
        y += 1
        array[x-1][y-1] = x * y

for i in array:
    print(i)