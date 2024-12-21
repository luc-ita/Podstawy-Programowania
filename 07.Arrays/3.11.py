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

print(bubble_sort([15,64,-9,13,54,9]))