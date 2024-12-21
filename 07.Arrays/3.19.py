arr = [7, 3, 8, 5, 2]

given_value = int(input("Enter a value: "))
count = sum(1 for num in arr if num > given_value)

print("Number of elements greater than", given_value, ":", count)