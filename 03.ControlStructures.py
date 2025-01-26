#1.3
###
# Checking whether a car exceeded the speed limit
#
speed_limit = 140
car_speed = int( input('Enter car speed (km/h): ') )

if car_speed > speed_limit:
    print(f'Your speed is {car_speed}km/h')
    print('Warning: speed limit exceeded!!')

#1.4
###
# Credit card payment 
#
account_balance = 500
total_payment = int(input (f'How many you want to pay: '))

if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')

#1.5
###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
total_tasks = 20
tasks_ok = int(input(f'How many tasks is completed: '))
test_passed = False

if tasks_ok >= total_tasks*0.5  :
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')

#1.6
###
# Checking whether the number
# entered from the keyboard is even or odd 
#
number = int(input('Enter number: '))

if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')

#1.7
###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = basic_salary
bonus = 0.15 # 15%
is_bonus = input('Does the employee receive a bonus? (Y/N):') == 'Y'
which_bonus =True

if is_bonus:
    which_bonus = input('Which bonus did he get? 15/30:') == '30'
    if which_bonus:
        bonus = 0.3 # 30%
    total_salary = basic_salary + basic_salary * bonus

print('Basic salary: ', basic_salary)
print('Bonus included? ', is_bonus)
print('Total salary: ', total_salary)

#2.2
###
# A program for checking clothing sizes
# S: Small size, M: Medium size, L: Large size
# XL: Extra large size or Incorrect symbol (if entered symbol
# dirrerent than S, M, L, XL)
#
size = input('Enter size symbol: ')

if size == 'S':
    print('S: Small size')
elif size == 'M':
    print('M: Medium size')
elif size == 'L':
    print('L: Large size')
elif size == 'XL':
    print('XL: Extra large size')
else:
    print('Incorrect symbol')

#2.3
###
# The car has three driving modes: Auto (A), Manual (M) and Eco (E).
# In each of these three modes, the average fuel consumption in liters
# per 100 km is 7, 9 and 6 respectively. Write a program that calculates
# total fuel consumption for a given distance in km and a given
# driving mode.
#
driving_mode = input('Enter driving mode (A/M/E): ')
distance = int(input('Enter distance in km: '))

if driving_mode == 'A':
    fuel_consumption = 7 # liters per 100km
elif driving_mode == 'M':
    fuel_consumption = 9 # liters per 100km
elif driving_mode == 'E':
    fuel_consumption = 6 # liters per 100km
else:
    driving_mode = False
    print('Unknown_data')

if driving_mode:
    total_consumption = fuel_consumption / 100 * distance
    print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')

#2.4
###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = int(input('First number: '))
number2 = int(input('Second number: '))
operator = str(input('Operator: '))

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '/':
    result = number1 / number2
elif operator == '*':
    result = number1 * number2

# print result
print(f'{number1} {operator} {number2} = {result}')

#2.5
###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1..12): '))

if month >= 10:
    quarter = 4
elif month >= 7:
    quarter = 3
elif month >= 4:
    quarter = 2
elif month >= 1:
    quarter = 1
else:
    quarter = False

print(f'Month {month} is in quarter {quarter}')

#2.6
number = int(input('Enter the number: '))
if number > 0:
    print(f'Number {number} is positive')
elif number < 0:
    print(f'Number {number} is negative')
elif number == 0:
    print('Number is 0')

#3.2
###
# Checking login and password
#
login = 'joe'
password = 'abcd'
entered_login = input('Login: ')
entered_password = input('Password: ')
if login == entered_login and password == entered_password:
    print('You are logged in')
else:
    print('Incorrect login or password!!')

#3.3
###
# Checking if discount is available
# The discount is available to children under 18,
# or people 65 or older.
#
age = int(input('Enter your age: '))

if age < 18 or age >= 65 :
    print('You have a discount')
else:
    print('You do not have a discount')

#3.4
###
# Checks whether at least one number entered
# from the keyboard is not negative
# 
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

if not x < 0 or y >= 0:
    print(f'At least one of the numbers {x} and {y} is not negative')

#3.5
###
# Calculates the number of days in a month
#
month = int(input('Enter month number (1..12): '))

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    days = 31 ## months with 31 days
elif month==4 or month==6 or month==9 or month==11:
    days = 30 ## months with 30 days
elif month == 2:
    days = 28 ## February 28 days 

print(f'Month {month} has {days} days')

#3.6
###
# Checks if the given day number of the month is correct
#
month = int(input('Enter month number (1..12): '))
day = int(input('Enter the day number of the month: '))
day_ok = False

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    days = 31 ## months with 31 days
elif month==4 or month==6 or month==9 or month==11:
    days = 30 ## months with 30 days
elif month == 2:
    days = 28 ## February 28 days 

if day > 0 and day <= days:
    day_ok = True

if day_ok:
    print('Given day number of the mont is correct')
else:
    print('Given day number of the mont is incorrect')

#4.3
for i in range(6):
    print('Practice makes perfect!')

#4.4
###
# Prints the name of university where you are studying
# with an extra space between characters (add a space between
# each character), e.g.
# 'book' -> 'b o o k'
#
university = 'Krakow University of Economics'
university_expanded = ''

for char in university:
    university_expanded = university_expanded + char + " "

print(university) # original university name
print(university_expanded) # expanded university name

#4.5
###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    char_new = ord(char)
    # add one to the character's code
    char_new = char_new + 1
    # corresponding character (use chr())
    char_new = chr(char_new)
    # add encrypted character to encrypted text
    encrypted_text = encrypted_text + char_new

print(plain_text)
print(encrypted_text)

#4.6
###
# Calculates the sum of integer numbers in the range <1,5>
#
sum = 0

for i in range(5,11):
    sum +=  i

print(f'Sum is {sum}')

#4.7
###
# Calculates the sum of even numbers in the range <1,10>
#
sum = 0

for i in range(1,11):
    if i%2:
        sum += i
    

print(f'Sum of even numbers in the range <1,10> is {sum}')

#4.8
###
# Calculates values for the following fractions: 1/2, 1/3, ..., 1/10
#
for i in range(1,11):
    print(f'1/{i} =', 1/i)

#5.3
###
# Prints a greeting
#
name = ''

while name == '':
    name = input('Enter your name: ')

print(f'Hello {name}')

#5.4
###
# A simple number guessing game
#
import random

# Randomly chosen number to be guessed from 1 to 100
number_to_guess = random.randint(1, 100)
user_guess = 0

print("Guess the number between 1 and 100!")

while user_guess != number_to_guess:
    user_guess = int(input("Enter your guess: "))

    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")

#5.5
###
# Sums numbers entered by user and aritmetic mean
#
total_sum = 0
i = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        arit_mean = total_sum / i
        break  # Exit the loop when 0 is entered
    total_sum += number
    i += 1

print(f"The total sum of the numbers is: {total_sum}")
print(f"The arithmetic mean of the numbers is: {arit_mean}")

#5.6
###
# Calculates the sum of even numbers from 1 to a given number N
#
N = 10
NN = N
sum_even = 0

# Calculate the sum of even numbers
while N:
    if not N % 2 == 0:
        sum_even += N
    N -= 1

print(f"The sum of even numbers from 1 to {NN} is: {sum_even}")

#5.7
###
# Takes a number from the user and counts down to zero.
#
# Modify the program so that the last five seconds of the counter
# are displayed in words, i.e. five, four, three, two, one.
#
import time

countdown = int(input("Enter the number of seconds to count down: "))

while countdown > 5:
    print(countdown)
    countdown -= 1
    time.sleep(1)  # Wait for 1 second

while countdown > 0:
    if countdown == 5:
        print('five')
    elif countdown == 4:
        print('four')
    elif countdown == 3:
        print('three')
    elif countdown == 2:
        print('two')
    elif countdown == 1:
        print('one')
    countdown -= 1
    time.sleep(1)  # Wait for 1 second

print("Time's up!")

#5.8
###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
error = True
while error:
    pin = str(input('Enter PIN: ')) # initial 4-digit PIN code
    i = 0
    for char in pin:
        i += 1
    if pin.isdigit() and i == 4:
        print('PIN correct')
        error = False
    else:
        print('PIN incorrect')
        error = True



while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        i = 0
        for char in pin:
            i += 1
        if pin.isdigit() and i == 4:
            print('PIN correct')
        else:
            print('PIN incorrect')
    elif choice == '5':
        error = True
        while error:
            pin = str(input('Enter the new PIN: '))
            i = 0
            for char in pin:
                i += 1
            if pin.isdigit() and i == 4:
                print('PIN correct')
                error = False
            else:
                print('PIN incorrect')
                error = True
        
    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    else:
        print("Invalid option. Please try again.")


#6.2
###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0
i = 0
# Count vowels in the text
while i < len(text):
    if text[i] in vowels:
        vowel_count += 1
    i += 1

print(f"The number of vowels in the text is: {vowel_count}")




#6.3
###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = False # False - switch off, True - switch on
light_switch2 = False
bulbs_on = 0
if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 2
print(f'{bulbs_on} are on')

#6.4
###
# Password validator
# New password is at least 12 characters long
#
new_password = input('Enter new password: ')
if len(new_password) < 12:
   print('Password too short (min. 12 chars)')

#6.5
###
# Program that simulates the operation of an electronic thermometer.
#
temperature = int(input("Enter a temperature: "))
if temperature > 35:
    print("It is extermely hot")
elif temperature > 30:
    print('It is hot')
elif temperature >= 15:
    print('It is warm')
elif temperature >= 0:
    print('It is cold')
else:
    print ("Warning, frost")

#6.6
###
#
time = int(input("How many hours you want to stay here: "))
sum = 0
while time != 0:
    if time > 6:
        cost = 20
    elif time >= 3:
        cost = 15
    elif time >= 1:
        cost = 5
    sum = sum + cost
    time -= 1
print(f'You will pay {sum} PLN by parking')

#6.7
###
#
age = int(input("How old are you: "))
if age >= 65:
    group = 'senior'
elif age >= 20:
    group = 'adult'
elif age >= 13:
    group = 'teen'
elif age < 13:
    group = 'child'

print(f'You are {group}')

#6.8
###
# Checking if both people are adults
#
person1_name = input('Enter first person name: ')
person1_age = int(input('Enter first person age: '))
person2_name = input('Enter second person name: ')
person2_age = int(input('Enter second person age: '))
if person1_age >= 18 and person2_age >= 18:
    print(f'Both {person1_name} and {person2_name} are adult')
else:
    print(f'Either{person1_name} or {person2_name} is not an adult')

#6.9
###
#
name = input('Enter name: ')
if name[-1] == 'a':
    print(name, 'is a Polish female name')
else:
    print(name, 'is not a Polish female name')

#6.10
###
#
hdog = int(input("Enter the dog's age in human years: "))
a=0
ddog = 0
while hdog != a:
    if a < 2:
        ddog += 10.5
    else:
        ddog += 4
    a += 1
    print(ddog)
print(f"The dog's age in dog's years is {ddog} years.")

#6.11
###
#
current = 140
prev = 200
if current < prev:
    print('Buy the product!!')
    print(f'Product price reduced by {(prev - current)/prev * 100}%')

#6.12
###
#
number = int(input('Number of products purchased: '))
price = int(input('Product price: '))
extra = 0
if number > 2:
    extra = number - 2

total = 2 * price + extra * price * 0.75
print(f'Ammount to pay: {total}')

#6.13
###
#
car_speed = int(input('Enter car speed: '))
speed_limit_min = 40
speed_limit_max = 140
if car_speed > speed_limit_max or car_speed < speed_limit_min:
    print('Warning: invalid car speed!!')

#6.14
###
#
facebook = input('Do you have facebook? (Empty if not): ')
twitter = input('Do you have twitter? (Empty if not): ')
instagram = input('Do you have instagram? (Empty if not): ')
if (bool(facebook) + bool(twitter) + bool(instagram)) >= 2:
    print('You are a good influencer!')

#6.15
###
#
ean = input('Enter EAN: ')
y = ''
z = 0
if len(ean) == 13 and ean.isdigit() == True:
    print('Ean is correct')
    if ean[0:3] == '590':
        print('Product is from Poland')
else:
    print('Ean is incorrect')

#6.16
###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:')
extra_rinse = input('Extra rinse? (y/n)')
extra_spin = input('Extra spin? (y/n)')
if program == 'j':
    total_washing_time += 40
elif program == 'u':
    total_washing_time += 70
elif program == 's':
    total_washing_time += 20
if extra_rinse == 'y':
    total_washing_time += 15
if extra_spin == 'y':
    total_washing_time += 9
print(f'Total washing time: {total_washing_time} minutes')

#6.17
###
time = input('Enter time (24-hour format): ')
if int(time[0:2]) > 12:
    hours = int(time[0:2]) - 12
    print(f'{hours}{time[2:5]}pm')
else:
    print(f'{time}am')

#6.18
###
x = int(input('Enter x: '))
y = int(input('Enter y: '))

if x > 0 and y > 0:
    qua = 'first quadrant'
elif x > 0 and y < 0:
    qua = 'second quadrant'
elif x < 0 and y < 0:
    qua = 'third quadrant'
elif x < 0 and y > 0:
    qua = 'forth quadrant'
else:
    qua = 'middle'

print(f'Point P({x},{y}) is in the {qua}  of the coordinate system')

#6.19
###
s= input('Are you interested in computer science? (y/n): ')
g= input('Do you like playing computer games? (y/n): ')
a= input('Do you have an Instagram account? (y/n): ')
if s == 'n':
    s = False
elif s == 'y':
    s =True
if g == 'n':
    g = False
elif g == 'y':
    g =True
if a == 'n':
    a = False
elif a == 'y':
    a =True

print(f'Interested in computer science: {s}')
print(f'Playing computer games: {g}')
print(f'Has an Instagram account: {a}')

#6.20
###
d = int(input('Enter the number: '))
b = ''
i = 16
while d != 0:
    r = d % 2
    b = (f'{r}{b}')
    d = d // 2
print(b)

#6.21
###
full = int(input('Enter the amount i PLN: '))
fives_r = full % 5
fives = (full - fives_r) / 5
twos_r = fives_r % 2
twos = (fives_r - twos_r) / 2

print(f'The amount of PLN {full} in coins:')
print('5 PLN coins:', fives)
print('2 PLN coins:', twos)
print('1 PLN coins:', twos_r)

#6.22
###
i = 0
while i < 30:
    i += 1
    if (i % 3) == 0 and (i % 5) == 0:
        print('BINGO')
    elif (i % 3) == 0:
        print('THREE')
    elif (i % 5) == 0:
        print('FIVE')
    else:
        print(i)

#6.23
###
x = int(input('Enter the number: '))
for i in range(10):
    i += 1
    print(f'{x} x {i} = {x * i}')

#6.24
###
for i in range(5):
    i += 1
    s= i * '*'
    print(s)
while i != 0:
    i -= 1
    s= i * '*'
    print(s)

#6.25
###
for i in range(9):
    i += 1
    s= i * str(i)
    print(s)

#6.26
###
pin = '0805'
user = input('Enter PIN: ')
for i in range(2):
    if user != pin:
        print('Wrong')
        user = input('Enter PIN: ')
if user == pin:
        print('Correct')
else:
     print('Sorry, your payment card has been blocked.')

#6.27
i = 6
while i > -1:
    for j in range(1,4):
        print(f'{i+j}',end=' ')
    i -= 3
    print()


#6.28
a = 0
b = 1
print(a)
print(b)
for i in range(18):
    c = a + b
    a = b 
    b = c
    print(c)


#6.29
max = int(input('Wpisz zakres: '))
for check in range(2, max):


##    check = int(input("Wpisz sprawdzana liczbe: "))  
    for i in range(2,check): ## sprawdzanie czy dana liczba jest pierwsza i jej drukowanie
        if (check % i) == 0:  ## podzieliła się bez reszty - wychodzimy z for'a bez else
            break
    else:                   ## wchodzimy po zrobieniu fora
        print(check)
        


#6.30
for i in range(1,8):
    for j in range(7):
        x = i + 7 * j
        print(x, end=' ')
    print()

#6.31
import random
for i in range(20):
    x = random.randint(5,10)
    print(x, end =' ')
