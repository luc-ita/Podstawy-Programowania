filename = 'it_company.csv'

with open(filename) as f:
    text = f.readlines()
for i, lines in enumerate(text):
    if (i % 5) == 0:
        input( 'Press Enter key...\n')
    print(lines)
    
