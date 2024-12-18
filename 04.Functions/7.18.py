def f(sentence):
    result = ''
    for i in sentence:
        if i != ' ':
            result += i
    return result
sentence = input()
print(f(sentence))