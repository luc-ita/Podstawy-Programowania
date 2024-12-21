array = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
input()
for i in array:
    print(i)

first = list(array[0])
last = list(array[len(array)-1])

array[0] = last
array[len(array)-1] = first

print()
for i in array:
    print(i)