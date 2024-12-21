# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements

food = 0
for i in monthly_expenses:
    food += i[0]

transport = 0
for i in monthly_expenses:
    transport += i[1]

utilities = 0
for i in monthly_expenses:
    utilities += i[2]

week_1 = 0
for i in monthly_expenses[0]:
    week_1 += i

week_2 = 0
for i in monthly_expenses[1]:
    week_2 += i

week_3 = 0
for i in monthly_expenses[2]:
    week_3 += i

week_4 = 0
for i in monthly_expenses[3]:
    week_4 += i

total = 0
for i in monthly_expenses:
    for j in i:
        total += j


# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food)
print('Transport:', transport)
print('Utilities:', utilities)
print('Week 1:', week_1)
print('Week 2:', week_2)
print('Week 3:', week_3)
print('Week 4:', week_4)
print('---------------')
print('TOTAL:', total)