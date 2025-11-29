import json

with open('./dogs.json','r',encoding="utf-8") as file:
    content=json.load(file)
for dog in content:
    if dog["age"]<5:
        for key,value in dog.items():
            print(f'{key} : {value}')
        print()