array = [2, 3, 2, 5, 8, 1, 9, 8]
unique= []
for i in array:
    if i in unique:
        False
    else:
        unique.append(i)

print(unique)