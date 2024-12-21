car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]

def bubble_sort(table):
    n = len(table)
    again = True
    while again == True:
        again = False
        for i in range(n-1):        
            if table[i] > table[i+1]:
                x = table[i]
                table[i] = table[i + 1]
                table[i + 1] = x
                again = True
    return table


print(bubble_sort(car_fuel_consumption))
print(bubble_sort(bank_transactions))