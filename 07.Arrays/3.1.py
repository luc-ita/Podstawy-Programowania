array = [34,7,19,4,21,8]
i = 0
sum = ''
while i < len(array):
    if array[i] % 2 == 0:
        sum += f'{array[i]} '
    i += 1

print(sum)
