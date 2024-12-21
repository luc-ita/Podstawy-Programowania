array = [   [7, 3, 7, 9, 0],
            [2, 9, 0, 1, 5],
            [3, 8, 6, 4, 7],
            [8, 7, 1, 1, 5]
        ]
sum = 0
last = len(array[0]) - 1
for i in array:
    sum += i[last]
print(sum)