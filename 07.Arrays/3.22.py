import random
arr = [7,9,2,4,5,6]

def rand_ele(array):
    x = array[random.randint(0,(len(array)-1))]
    return x

print(rand_ele(arr))