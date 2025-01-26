import json

basic_data = {
    "name": "Barbara",
    "age": 21
}

advanced_data = {
    "status": "student",
    "married": False,
    "interest": ["reading", "swimming"]
}



person = basic_data | advanced_data
print(json.dumps(person, indent=4))
