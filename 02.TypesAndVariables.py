###
# 3.1
#
company = "ABC Data"
phone = "555-123-009"
employees = 25
remote_work = True
big_company = employees > 100
income = 4500000
income_per_person = income / employees

print("Variable `company` has value: ", company)
print("and is", type(company))
print("Variable `phone` has value: ", phone)
print("and is", type(phone))
print("Variable `employees` has value: ", employees)
print("and is", type(employees))
print("Variable `remote_work` has value: ", remote_work)
print("and is", type(remote_work))
print("Variable `big_company` has value: ", big_company)
print("and is", type(big_company))
print("Variable `income` has value: ", income)
print("and is", type(income))
print("Variable `income_per_person` has value: ", income_per_person)
print("and is", type(income_per_person))


###
# 3.2
# A program that calculates the sum of two numbers.
# Modify the program to calculate the sum of three numbers.
#
number1 = 71
number2 = 14
number3 = 25
result = number1 + number2 + number3
print('Number 1: ', number1)
print('Number 2: ', number2)
print('Number 3: ', number3)
print('The result of summation: ', result)


###
# 3.3
# A program for swapping two varable values
#
x = 7
y = 34
z = 0 # additional, auxiliary variable
print("Before swapping: x=", x, "y=", y)

# swap the values
z = x
x = y
y = z

print("After swapping: x=", x, "y=", y)


###
# 3.4
# A program that, for a given speed in km/h,
# prints the speed in m/s
speed_kmh = 70
speed_ms = speed_kmh * 1000 / 3600
print(speed_kmh, "km/h = ", speed_ms, "m/s")

###
# 3.5
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
import math
a = 5
b = 8
diagonal = math.sqrt(a**2 + b**2)
print("We have rectangle with sides ", a, " and ", b)
print("Diagonal is ", diagonal)


###
# 3.6
# Program that calculates the distance 
# to the horizon from a height given
import math

height = input("Enter your height in m: ")
height = float(height)
d = 3.57 * math.sqrt(height)
print("Distance you see on a beach is: ", d, "km")
height = height + 20
d = 3.57 * math.sqrt(height)
print("Distance you see from hotel is: ", d, "km")


###
# 3.7
# A program that calculates and prints:
# - the number of people and percentage of the total
#   population living in the Northern Hemisphere
# - the number of people and percentage of the total
#   population living in the Southern Hemisphere
#
total = 8000000000
north = 7200000000
south = total - north
print("World population: ", total)
print("Northern Hemisphere: ", north)
print("Northern Hemisphere in %: ", north/total*100)
print("Southern Hemisphere: ", south)
print("Nouthern Hemisphere in %: ", south/total*100)


###
# 3.8
# A program that calculates and prints
# the average grade of a student
#
math = 5
art = 4
music = 5
history = 3
average = (math + art + music + history) / 4
print("Average grade is", average)


###
# 4.1
# Printing student's personal data
#
name = "Adam"
age = 24
height = 180
future_age = age + 6
print(f"My name is {name}.")
print(f"I am {age} years old, and my height is {height} cm.")
print(f"In 6 years I will be {future_age} years old.  ")


###
# 4.2
# Write a program that calculates and prints
# the income of a family per person. To print the results
# in a readable form, use f-strings.
#
father_income = 5450
mother_income = 4920
family_members = 5
total_income = father_income + mother_income
income_per_person = total_income / family_members
print(f'Total family income is {total_income}, and income per person is {income_per_person}')


###
# 4.3
#
a = 3
b = 5
print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={a/b}')


###
# 5.1
# A program that reads your first and last name from the keyboard.
# Store this data in two separate variables.
# Then, print your full name i.e. first and last name separated by a single space.
#
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
full_name = first_name + ' ' + last_name
print(f'Your first name is {first_name} and your last name is {last_name}')
print(f'And your full name is {full_name}')


###
# 5.2
# A program to calculate the volume and surface area of ​​a cube.
# 
cube_side_string = input('Enter cube side: ')
cube_side = int(cube_side_string)
cube_volume = cube_side**3
cube_surface_area = cube_side**2 * 6
print(f'The volume of a cube with side {cube_side} is {cube_volume}')
print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}')


###
# 5.3
# A program to calculate the volume and surface area of ​​a cuboid.
# 
string_a = input('Enter cuboid side a: ')
a = int(string_a)
string_b = input('Enter cuboid side b: ')
b = int(string_b)
string_c = input('Enter cuboid side c: ')
c = int(string_c)
cuboid_volume = a *b *c
cuboid_surface_area = a*b*2 + a*c*2 + b*c*2
print(f'The volume of a cuboid with sides {a}, {b}, {c} is {cuboid_volume}')
print(f'The surface area of a cuboid with sides {a}, {b}, {c}  is {cuboid_surface_area}')

###
# 5.4
# A program to calculate the VAT.
# 
a = input('Enter ammount: ')
b = int(a) * 0.23
print()
print(f'Your ammount : {a}')
print(f'Your VAT     : {b}')

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

###
# 6.1
# A program that calculates the number of characters
# of your name, surname and full name
#
name = 'Luca'   # replace Anna with your name
surname = 'Gorzkowski' # replace May with your surname
characters_in_name = len(name)
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {len(surname)} characters')
print(f'Your full name has {len(name + surname)} characters') # with a space between name and surname

###
# 6.2
# A program that prints your initials
#
name = 'Luca'
surname = 'Gorzkowski'
print(name[0], surname[0])

###
# 6.3
# A program that find and show upper letters:
#
university = "Krakow University of Economics"
for letter in university:
   if letter.isupper():
      print(letter)

      ###
# 6.4
# A program for printing detailed information.
#
employee = "Mr. John May, born on 1998-02-16"
print(f'Name: {employee[4:8]}')
print(f'Surname: {employee[9:12]}')
print(f'Born: {employee[22:35]}')
print(f'Initials: {employee[4]} {employee[9]}')

###
# 6.5
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone = input('Enter phone number: ')
print(f'Phone number: {phone[0:3]}-{phone[3:6]}-{phone[6:9]}')

###
# 6.6
# A program to print numerical representations of characters.
#
print(f'a {ord('a')}')
print(f'b {ord('b')}')
print(f'z {ord('z')}')
print(f'A {ord('A')}')
print(f'B {ord('B')}')
print(f'Z {ord('Z')}')
print(f'! {ord('!')}')
print(f'= {ord('=')}')
print(f'+ {ord('+')}')
print(f'€ {ord('€')}')

###
# 6.7
# A program that prints a numerical representation of each letter of your name.
#
name = 'Luca' # replace John with your name
print(f'The letter {name[0]} has a code {ord(name[0])}')
print(f'The letter {name[1]} has a code {ord(name[1])}')
print(f'The letter {name[2]} has a code {ord(name[2])}')
print(f'The letter {name[3]} has a code {ord(name[3])}')

###
# 6.8
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter second letter: ')
first_letter_code = ord(first)
second_letter_code = ord(last)
number_of_letters = second_letter_code - first_letter_code - 1
print(f'Between {first} and {last} is {number_of_letters} letters')

###
# 6.9
# Character code conversion
#
print('67', chr(67))
print('111', chr(111))
print('111', chr(111))
print('108', chr(108))
print('33', chr(33))
print()
#or
print(chr(67),chr(111),chr(111),chr(108),chr(33))


###
# 6.10
# String manipulation
#
movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print(movie.upper())

# print title in small letters
print(movie.casefold())

# print how many times the vowel "e" appears in the title
print(movie.count("e"), ' of e')

# print where in the text is the word "Lord"
print('Lord is on', movie.find("Lord"))

# print where in the text is the word "dragon"
if (movie.find("dragon")) == -1:
    print('There is no dragon in this title')
else:
    print('dragon is on', movie.find("dragon"))

###
# 7.1
# People up to and including 26 years of age are exempt
# from paying taxes in Poland. Write a program that,
# based on the person's age entered from the keyboard,
# prints True if the person is exempt from paying taxes
# and prints False otherwise.
#
age = int(input('Enter age: '))
no_tax = age < 27
print(f'Exemption from paying taxes: {no_tax}')

###
# 7.2
# A program that checks whether the password length
# read from the keyboard is correct.
#
password = input('Enter password: ')
password_ok = len(password) >= 8
print(f'Password length is valid: {password_ok}')

###
# 7.3
# A program that checks whether the number entered
# from the keyboard is even.
# A number is even if the remainder when divided by 2 is 0.
# What operator do you need to use to calculate
# the remainder of division?
#
number = int(input('Enter number: '))
modulo = number % 2
print(modulo == 0)

###
# 7.4
# A program that , based on the circumference of the tree 
# entered from the keyboard, calculates and prints 
# the value True if the tree can be cut down, or print 
# the value False otherwise. 
#
c = int(input('Enter tree circumference in cm: '))
d = c/3.14
print(d <= 50)

###
# 7.5
# Vehicle registration numbers in Krakow start
# with the letters KR or KK. Write a program that checks
# whether the vehicle registration number entered
# from the keyboard means a vehicle from Krakow.
# Print True whether a car is from Krakow or False otherwise.
#
car_number = input('Enter car registration number: ')
car_number = car_number.upper()
is_krakow = car_number[0:2] == "KR" or car_number[0:2] == "KK"
print(f'Car is from Krakow: {is_krakow}')

###
# 7.6
# A program that checks whether the vehicle speed 
# entered from the keyboard is correct.
#
s = int(input('Enter vehicle speed: '))
print(s > 40 and s < 140)

###
# 7.7
# A program that generate random number in the range(5,10).
#
import random
random_number = random.randint(5,10)
print(random_number)

###
# 7.8
# A program that prints results of three dice rolls
# and the sum of dice rolled.
#
import random
dice_roll_1 = random.randint(1,6)
dice_roll_2 = random.randint(1,6)
dice_roll_3 = random.randint(1,6)
total = dice_roll_1 + dice_roll_2 + dice_roll_3
print('Sum of dice rolled:', total)

###
# 7.9
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

###
# 7.10
# A program that enables a user to challenge a computer.
# The computer throws dice. Then, the user then tries to guess
# the number from dice by entering a number from 1 to 6
# from the keyboard. If the user has guessed the number
# from the dice, the computer prints True. Otherwise,
# the computer prints False.
#
import random
# COMPUTER TURN
computer = random.randint(1,6)
# YOUR TURN
you = int(input('Guess the number: '))
print(f'{you == computer} It was {computer}')

###
# 8.2
# Calculation of circle area and circumference 
#
r = int(input('Enter the radius: '))
pi = 3.14
c = round(2 * pi * r, 2)
a = round(pi * r * r, 2)

print(f'Circumference = {c}')
print(f'Area =  = {a}') 

###
# 8.3
# Calculation of temperature
#
c = int(input('Enter the temmperature: '))
f = round(9 / 5 * c + 32, 2)
k = c + 273.15
print(f' There is {f} degrees Fahrenheit or {k} Kelwins')

###
# 8.4
# A program that prints your height both in cm and in feet and inches.
#
cm = int(input('Enter your height in cm: '))
feet = cm // 30.4
inches = cm // 2.54
feetmod = cm % 30.4
inchesmod = cm % 2.54
print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')
print(f'Reaminders are {feetmod} feet and {inchesmod} inches')

###
# 8.5
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#
swift = input('Input your SWIFT cdoe: ')
print(f'Bank Code: {swift[0:4]}')
print(f'Country Code: {swift[4:6]}')

###
# 8.6
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#
distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input ('Enter fuel consumption in liters per 100 km: '))
total_fuel_consumption = distance * fuel_consumption / 100
total_cost = fuel_price * total_fuel_consumption
print(f'Total fuel consumption: {total_fuel_consumption}')
print(f'And you will pay: {total_cost}')

###
# 8.7
# Powerful program to convert decimal to binary and hexagonal
dec = int(input('Enter number: '))
bin = bin(dec)
hex = hex(dec)
print(f'This number in binary number is: {bin} and in the hexagonal is: {hex}')
