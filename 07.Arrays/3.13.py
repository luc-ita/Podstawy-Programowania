def f(number, array):
    if number in array:
        return True
    else: 
        return False
    
number = int(input())
array = [15, 38, 7, 23, 14]
print(f(number, array))