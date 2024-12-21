def f(amount_to_pay):
    coins = 0
    coins += amount_to_pay // 5
    rest = amount_to_pay % 5
    coins += rest // 2
    rest = rest % 2
    coins += rest
    return coins

amount_to_pay = int(input())
print(f'f({amount_to_pay}) returns {f(amount_to_pay)}')