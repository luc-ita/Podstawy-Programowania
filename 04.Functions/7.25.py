def f(x,y):
    sum = 0
    for i in range(x,y+1):
        if i%2 == 0 and i%3 == 0 and i%4 != 0:
            sum += i
    return sum

x = int(input('x: '))
y = int(input('y: '))
print(f(x,y))
