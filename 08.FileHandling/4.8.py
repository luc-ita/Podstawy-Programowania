with open("files.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    name, extension = line.rsplit('.', 1)
    if len(extension) == 4:
        print(line)
