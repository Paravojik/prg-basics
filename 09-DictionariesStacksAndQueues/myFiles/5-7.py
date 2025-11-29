hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

def hotel_list(hotels):
    print('Hotels in Krakow: ',end="")
    for i in range(len(hotels)-1):
        print(hotels[i]['name'], end=", ")
    print(hotels[-1]['name'])

def avg_price(hotels):
    total=0
    for i in hotels:
        total+=i['price']
    print(f'Average hotel price in Krakow: {round(total/len(hotels),2)}')

def cheaperHotel(*arg):
    hotels=[]
    for i in arg:
        for j in i:
            hotels.append(j)
    hotels=sorted(hotels,key=lambda x:x['price'])
    print('Cheaper hotels is: '+hotels[0]['name'])



hotel_list(hotels_in_Krakow)
avg_price(hotels_in_Krakow)
hotel_list(hotels_in_Sopot)
avg_price(hotels_in_Sopot)
cheaperHotel(hotels_in_Krakow,hotels_in_Sopot)