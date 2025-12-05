class C:
    def __init__(self,coords):
        self.coords=coords

    def m(self,n):
        count=0
        for i in self.coords:
            if i[0]>0 and i[1]>0:
                count+=1
        return True if count>=n else False
    


arr=C([[2,3],[1,8],[-6,4],[3,-7]])


print(arr.m(2))
print(arr.m(3))

        
