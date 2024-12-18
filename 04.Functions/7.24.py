def f(expression):
    alpha = 0
    beta = 0
    charlie = 0
    count = 0
    for i in expression:
        if count == 0:
            alpha = int(i)
            count += 1
        elif count == 1:
            beta = i
            count += 1
        elif count == 2:
            charlie = int(i)
            if beta == '+':
                alpha = alpha + charlie
            elif beta == '-':
                alpha = alpha - charlie
            count = 1
    return alpha

expression = input()
print(f'= {f(expression)}')
