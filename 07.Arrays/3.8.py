array = [2, 6, 4, 9, 7]
def star(n):
    for i in n:
        print(f'{i}: {i * '*'}')
    return

star(array)