import csv

filename = 'it_company.csv'

with open(filename, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['Job Title'] == 'Graphic Designer':
            print(f"{row['First Name']} {row['Last Name']}, {row['Email']}")
