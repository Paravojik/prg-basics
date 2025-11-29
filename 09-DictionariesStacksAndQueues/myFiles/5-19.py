import json

def numberOfRooms(d):
    return len(d)
def numberOfPaidReservation(d):
    total=0
    for i in d:
        if i['paid']==True:
            total+=1
    return total
def numberOfUnpaidReservation(d):
    return numberOfRooms(d)-numberOfPaidReservation(d)

def valueOfPaidReservation(d):
    total=0
    for i in d:
        if i['paid']==True:
            total+=i['price_per_night']*i['nights']
    return total

def valueOfUnpaidReservation(d):
    total=0
    for i in d:
        if i['paid']==False:
            total+=i['price_per_night']*i['nights']
    return total


with open('./reservations.json','r',encoding='utf-8') as file:
    data=json.load(file)['reservations']

print('Number of rooms:',numberOfRooms(data))
print('Number of paid rooms:',numberOfPaidReservation(data))
print('Number of unpaid rooms:',numberOfUnpaidReservation(data))
print('Value of paid rooms:',valueOfPaidReservation(data))
print('Value of unpaid rooms:',valueOfUnpaidReservation(data))
