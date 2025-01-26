person = {
    "name": "Marek",  # str
    "surname": "Banach",  # str
    "age": 25,  # int
    "hobby": ["swimming", "excursions"],  # list
    "married": True,  # bool
    "phone": {"landline": "123444321",  # dict
              "mobile": "777888999"}
}

print("Name:", person["name"])
print("Hobby:", person["hobby"])
print("\nEntire Dictionary:")
print(person)


person["surname"] = "Nowak"
person["married"] = not person["married"]
person["gender"] = "male"
person["hobby"].append("bicycle")
person["phone"]["work"] = "313131444"


print("\nUpdated Dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")