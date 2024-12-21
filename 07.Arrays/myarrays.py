def f1(array):
    a = array[0]
    b = array[0]
    for i in array:
        if i > a:
            a = i
        elif i < a and i > b:
            b = i
    return b

def f2(array):
    small = array[0]
    big = array[0]
    for i in array:
        if i < small:
            small = i
        elif i > big:
            big = i
    return small, big

def f3(array):
    table = list(array)
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
    if (n % 2) != 0:
        a = n//2
        mediana = table[a]
    else:
        a = n/2
        b = a-1
        mediana = (table[a] + table[b])/2

    return mediana



def f4(array):
    x = ''
    for i in array:
        if x == '':
            x += str(i)
        else:
            y = '-' + str(i)
            x += y
        
    return x