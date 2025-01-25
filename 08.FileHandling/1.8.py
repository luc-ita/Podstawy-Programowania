with open('pets.txt') as f:
    content = f.read()

print(content)

words = content.split()
print('Word count:', len(words))

