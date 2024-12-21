array1 = [1, 2, 3]
array2 = [1, 2, 3, 4, 5]
result = True

for i in array1:
    if i not in array2:
        result = False
        break

print("Array1:", array1)
print("Array2:", array2)
print("Array1 is a subset of Array2:", result)