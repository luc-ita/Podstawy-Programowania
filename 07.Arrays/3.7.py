array = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
win = ''
for i in array:
    if len(i) > len(win):
        win = i
print('Longest name: ', win)