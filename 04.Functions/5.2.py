mode = int(input('1. Cm to inches. \n2. Feet ro cm. \n3. Inches to cm \n\nEnter mode: '))
import converters
len_unit = int(input("Enter lengh: "))
if mode == 1:
    print(f'{len_unit} cm is {converters.cm_to_inch(len_unit)} inches')
if mode == 2:
    print(f'{len_unit} feet is {converters.feet_to_cm(len_unit)} cm')
if mode == 3:
    print(f'{len_unit} inches is {converters.inch_to_cm(len_unit)} cm')
