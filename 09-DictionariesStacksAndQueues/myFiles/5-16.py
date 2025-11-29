import json

json_path='./computer.json'
with open(json_path,'r', encoding='utf-8') as file:
    computer_data=json.load(file)
for i,j in computer_data.items():
    print(f'{i} : {j}')