###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    i = 0
    for i, line in enumerate(file):
        print(f'{i+1}. {line}', end="")