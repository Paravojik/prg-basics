a=0
b=1
print(a, b,end=" ")
for i in range(1,21):
    b=a+b
    a=b-a
    print(b,end=" ")