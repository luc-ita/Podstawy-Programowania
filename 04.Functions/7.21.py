def f(num1,num2,num3):
    maxv = max(num1,num2,num3)
    minv = min(num1,num2,num3)
    result = maxv - minv
    return result

num1 = int(input('num1: '))
num2 = int(input('num2: '))
num3 = int(input('num3: '))
print(f'Difference is {f(num1,num2,num3)}')