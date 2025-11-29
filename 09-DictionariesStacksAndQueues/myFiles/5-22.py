import json


data={}
data['name']=str(input("Enter a name of puchased product: "))
data['price']=round(float(input("Enter the price of the purchased product: ")),2)
data['paid']=True if str(input("Enter if it is paid (yes/no): ")).lower()=='yes' else False

print(data)
product_path='./product.json'
with open(product_path,'r',encoding='utf-8') as file:
    existing_data=json.load(file)
existing_data.append(data)
with open(product_path,'w',encoding='utf-8') as file:
    json.dump(existing_data, file, indent=2)