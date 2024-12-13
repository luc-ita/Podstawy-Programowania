###
# 7.8
# A program that prints the number of dice rolled and 
# the value True if the number rolled is 1 or 6.
#
import random
d1 = random.randint(1,6)
d2 = random.randint(1,6)
d3 = random.randint(1,6)
d4 = random.randint(1,6)
print(d1, d2, d3, d4)
print()
print('Dice rolled: 4')
print(f'Special number (1 or 6): {d1 == 1 or d1 == 6 or d2 == 1 or d2 == 6 or d3 == 1 or d3 == 6 or d4 == 1 or d4 == 6}')
print('check')