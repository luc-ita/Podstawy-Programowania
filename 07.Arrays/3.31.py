array = [[-38, 19], [5,40],[-7,11],[29,16]]


min = [0][0]
max = [0][0]
min_pos = (0, 0)
max_pos = (0, 0)


for pos_x, i in enumerate(array):
    for pos_y,j in enumerate(i):
        if j < min:
            min = j
            min_pos = (pos_x, pos_y)

        if j > max:
            max = j
            max_pos = (pos_x, pos_y)
 


print(f"Minimum: {min} at position {min_pos}")
print(f"Maximum: {max} at position {max_pos}")