def f(number):
    num_str = str(number)
    digit_count = {}
    sum = 0
    
    for i in num_str:
        if i in digit_count:
            digit_count[i] += 1
        else:
            digit_count[i] = 1
    
    for i, count in digit_count.items():
        if count > 1:
            sum += int(i) * (count - 1)

    return sum

print(f(1027))
print(f(230335))
print(f(513553007))