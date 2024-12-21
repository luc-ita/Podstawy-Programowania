def f(x,y):
    sum = 0
    for i in range(x,y):
        if i < 0:
            if (i % 2) == 0:
                sum += 1
    return sum

x = int(input('Enter first number: '))
y = int(input('Enter last number: '))

print(f'f({x},{y}) returns {f(x,y)}')