basic_data = {
   "name":"Barbara",
   "age":21
}

advanced_data = {
   "status":"student",
   "married":False,
   "interest":["reading","swimming"]
}

person=basic_data
for key, value in advanced_data.items():
    person[key]=value
print(person)