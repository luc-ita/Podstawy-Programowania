array = [15, 8, 31, 47, 2, 19]
print(array)
total = 0
count = 0
while count < len(array):
    total += array[count]
    count += 1

total = total / len(array)
print(total)