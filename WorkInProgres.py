###
# 5.5
# A program to calculate the price and discount.
# 
ast = input(f'Enter price: ')
bst = input(f'Enter discount %: ')
a = float(ast)
b = int(bst)
c = round((100 - b) / 100 * a, 2)
d = round((a - c), 2)
print()
print(f'Price with discount: {c}')
print(f'Reduction: {d}')