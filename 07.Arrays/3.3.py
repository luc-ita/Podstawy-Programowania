array = [8, 2, 5, 1, 9]
input()
print(array)
count = 0
for i in array:
    x = i*i
    array[count] = x
    count += 1

print(array)