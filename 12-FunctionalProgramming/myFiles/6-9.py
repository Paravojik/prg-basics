arr={"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}


arr2=list(filter(lambda x:arr[x]>0,arr))

print("Cities with positive temperatures:"," ".join(arr2))