arr=[("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

arr2=list(map(lambda x:", ".join([x[0].upper(),x[1]]),arr))
for i in arr2:
    print(i)
