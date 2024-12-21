array = [15, 8, 31, 47, 2, 19]
array2 = [0 for z in range(len(array))]
input()
count = 0
for i in range(len(array)):
    x = 0 - i - 1
    array2[i] += array[x]
    count += 1

print(array2)