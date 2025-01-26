import json

# Dictionary describing Batman Begins
batman_info = {
    "title": "Batman Begins",
    "director": "Christopher Nolan",
    "year": 2005,
    "main_actors": ["Christian Bale", "Michael Caine", "Liam Neeson"],
    "genre": ["Criminal", "Adventure", "Drama"]
}


# Write the dictionary to a JSON file
with open('favourite.json', 'w') as file:
    json.dump(batman_info, file, indent=4)

