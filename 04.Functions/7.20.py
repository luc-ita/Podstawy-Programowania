def f(n):
    count = 0
    check = 1
    while count != n:
        check += 1

        for i in range(2,check): ## sprawdzanie czy dana liczba jest pierwsza i jej drukowanie
            if (check % i) == 0:  ## podzieliła się bez reszty - wychodzimy z for'a bez else
                break
        else:                   ## wchodzimy po zrobieniu fora
            count += 1
    return check

n = int(input())
print(f(n))
    