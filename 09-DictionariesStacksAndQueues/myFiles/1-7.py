store={
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}
amount=0
for item,quantity in store.items():
    amount+=quantity
    print(f'{item} : {quantity}')
print(f"Total amount: {amount}")