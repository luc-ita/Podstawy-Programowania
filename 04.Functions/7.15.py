def f(detector):
    last = ''
    count = 0
    result = False
    for i in detector:
        if i == last:
            count += 1
        else:
            count = 0
            last = i
        if count == 3:
            result = True
            break
    return result

detector = input('Enter sequence: ')
print(f(detector))