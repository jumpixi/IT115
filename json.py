import json

# Sample ata
data = {
    'name': 'John doe',
    'age': 30,
    'city': 'Seattle, WA',
    'interests': ['power', 'talking', 'Coding'],
    "is_student": True
}

# Writing data to a JSON file
with open('data.json', 'w') as json_file:

    json.dump(data, json_file, indent=4)
    
    #Im making a change to my file to prove that I just saved something