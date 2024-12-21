array =[-15, 8, -31, 47, -2, 19]
for i in range(1,len(array)):
    if array[i] < array[0]:
        array[0] = array[i]
    elif array[i] > array[1]:
        array[1] = array[i]
    
print('Min is: ', array[0])
print('Max is: ', array[1])