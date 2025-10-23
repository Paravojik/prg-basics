university = "Krakow University of Economics"
ans=university[0]
for i in range(len(university)-1):
    if university[i]==' ' and university[i+1].isupper():
        ans+=university[i+1]
print(ans)