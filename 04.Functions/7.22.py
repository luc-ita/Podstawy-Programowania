def f(name):
    j = 0
    result = name[0]
    for i in name:
        if i == ' ':
            result += name[j+1]
        j += 1
    return result

name = input()
print(f(name))

