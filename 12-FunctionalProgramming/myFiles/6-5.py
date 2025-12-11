arr=[i for i in range(1,21)]

arrF=list(filter(lambda x:(x%2==0 and x%3==0),arr))
print(arr)
print(arrF)