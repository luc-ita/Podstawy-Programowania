def f(number1,number2,operator):
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == '**':
        result = number1 ** number2
    elif operator == '*':
        result = number1 * number2
    elif operator == '%':
        result = number1 % number2
    return result

number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))
operator = input('Enter operator (  +,-,*,%,**  ): ')
print(f'Result is {f(number1,number2,operator)}')