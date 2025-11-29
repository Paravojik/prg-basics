import json



# Read the contents of the json file
with open('./voting_data.json', 'r',encoding='utf-8') as file:
    voting_data = json.loads(file.read())
print(voting_data)
# Vote for a person
person_name = input('Name of the person you are voting for:')
if person_name in voting_data:
    voting_data[person_name] += 1
else:
    voting_data[person_name]=1

# Save voting data to json file
with open('./voting_data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(voting_data))