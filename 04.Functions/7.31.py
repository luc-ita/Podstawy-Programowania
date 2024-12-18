def power(x, n):
    # x^0 == 1
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


result = power(5, 3)
print(result)