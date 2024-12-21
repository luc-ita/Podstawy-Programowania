abc = (50,20,40,50,30,50)
x = int(input('Enter searched number: '))
count = 0
for i in abc:
    if i == x:
        count += 1
print('Number of occurrences: ', count)
