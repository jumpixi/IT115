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
with open{'data.json', 'w'} as json_files:

    json.dump(data, json, indent=4)
    
    #Im making a change 