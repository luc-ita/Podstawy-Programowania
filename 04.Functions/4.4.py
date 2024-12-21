###
# Calculates the sum of the digits in a number
#
def sum_digits(any_number):
    result = 0
    for i in any_number:
            result += int(i)
    return result

any_number = str(abs(int(input('Enter integer number: '))))

result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')