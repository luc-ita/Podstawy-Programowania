def f(product_code):
    sum = 0
    count = 0
    result = False
    for i in product_code:
        if count == 3 and (sum%7) == int(i):
            result = True
            break

        else:
            sum += int(i)
            count += 1

    return result

product_code = input()
print(f(product_code))