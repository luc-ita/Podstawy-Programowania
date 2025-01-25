###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'


count = 0
with open(file_name) as f:
    for line in f.readlines():
        if job_title in line:
            count += 1
            print(f'{count}. {line}', end="")


