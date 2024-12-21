###
# Reads the entire contents of a file
#
def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

# reads the entire file and splits
file_content = read_from_file('pets.txt')
file_words = file_content.split()

# calculates the total number of words
total = len(file_words)

print('Total words:', total)