def f(n):
    sum = ''
    for i in range(n):
        sum += str(i+1)
    return sum
    
n = int(input())
print(f(n))