names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']





def sortFunc(arr):
    return sorted(arr, key= lambda x: x[1])


names2=sortFunc(names)


print("Sorted list: ")

for i in names2:
    print(i)
