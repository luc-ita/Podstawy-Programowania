def f(number, even):
    sum = 0
    for i in number:
        if even == 'True':
            if (int(i) % 2) == 0:
                sum += int(i)
        if even == 'False':
            if(int(i) % 2) == 1:
                sum += int(i)
    return sum

number = input('Enter the number: ')
even = input('Do you want sum only even? True/False: ')
print(f(number,even))
