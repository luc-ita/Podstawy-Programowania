def main(number):
    verdict = True
    for i in number:
        if i == '1' or i == '0':
            verdict = True
        else:
            verdict = False
            break
    return verdict