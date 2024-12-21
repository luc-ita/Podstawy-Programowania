###
# Reads the entire contents of a file
#
def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

# reads the entire file and splits lines into array
file_content = read_from_file('it_company.csv')
file_lines = file_content.splitlines()

# print employees as Software Enginner
for line in file_lines:
   if 'Software Engineer' in line:
      print(line)
