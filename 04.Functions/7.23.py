def f(password):
    checkin = ''
    result = True
    for i in password:
        if i in checkin:
            result = False
            break
        else:
            checkin += i
    if len(password) < 6:
        result = False
    return result

password = input('Enter password: ')
print(f(password))

