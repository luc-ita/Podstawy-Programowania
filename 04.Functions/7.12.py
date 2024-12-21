def f(n):
    sum = ''
    for i in range(n):
        sum += '*'
        if i != (n-1):
            sum += '/'
            
    return sum
    
n = int(input())
print(f(n))