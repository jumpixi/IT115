# Class Library
import json

# Sample Data
data = {
    'name': 'Conker Fur',
    'age': 30,
    'city': 'Twycross, UK',
    'interests': ['Having a good day', 'Talking', 'Binge'],
    "is_student": True
}

# Writing data to a JSON file
with open('data.json', 'w') as json_file:

    json.dump(data, json_file, indent=4)

print('Data has been written to data.json')


# Reading from the JSON file
with open('data.json', 'r') as json_file:
    # Load the Data
    loaded_data = json.load(json_file)

print('Data loaded from data.json')
print(loaded_data)




# Changing and appending the contents to the data.json file
loaded_data['age'] = 100
loaded_data['interests'].append ('They let me do what I want because my talent is that great')

with open('data.json', 'w') as json_file:
    json.dump(loaded_data, json_file, indent=4)

print('Modified data to the data.json file')