def f(text):
    result = ''
    count = 0
    for i in text:
        if count == 0:
            result += i
        else:
            result += '-' + i
        count += 1
          
    return result
    
text = input()
print(f(text))