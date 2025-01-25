with open("powers.txt", "w") as file:
    for i in range(1, 101):
        square = i ** 2
        cube = i ** 3

        result = f"{i},{square},{cube}"
        print(result)
        file.write(result + "\n")


