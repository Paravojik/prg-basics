person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}
print(person['name'])
print(', '.join(person['hobby']))
for i, j in person.items():
    print(f"{i} : {j}")

person['surname']="Nowak"
person['married']=not person['married']
person['gender']="male"
person['hobby'].append('bicycle')
person['phone']['work phone']='313131444'
for i, j in person.items():
    if type(j)==list or type(j)==dict:
        for l in person[i]:
            print(f"  - {l}")
    else:
        print(f"{i} : {j}")

