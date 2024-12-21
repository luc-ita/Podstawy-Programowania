categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

max_exp = max(expenses)
count = 0
while max_exp != expenses[count]:
    count += 1
print('Most expensive is', categories[count])