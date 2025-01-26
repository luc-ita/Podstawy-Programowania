import json

file_path = 'voting.json'


def read_voting_data(file_path):
    try:
        with open(file_path, mode='r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_voting_data(file_path, data):
    with open(file_path, mode='w') as file:
        json.dump(data, file, indent=4)



voting_data = read_voting_data(file_path)

person_name = input('Name of the person you are voting for: ').strip()
if person_name:
    voting_data[person_name] = voting_data.get(person_name, 0) + 1
    print(f"Vote recorded for {person_name}. Current votes: {voting_data[person_name]}")
else:
    print("No name provided. Vote not recorded.")

save_voting_data(file_path, voting_data)
print("Voting data saved successfully.")

