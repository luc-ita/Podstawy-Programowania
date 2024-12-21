arr = [7, 9, 2, 4, 5, 6]

evens = []
odds = []

for num in arr:
    if num % 2 == 0:
        evens.append(num)

for num in arr:
    if num % 2 != 0:
        odds.append(num)

sorted_arr = evens + odds

print("Original array:", arr)
print("Evens first:", sorted_arr)