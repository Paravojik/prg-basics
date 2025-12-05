class C:
    def __init__(self,stadium):
        self.arr=stadium

    def m1(self,s,n):
        self.arr[s]=n

    def m2(self,s):
        values=[i for i in s]
        ans=0
        for i in values:
            if i in self.arr:
                ans+=self.arr[i]
        return ans
    
    def show(self):
        print(self.arr)


st1=C({"A":120,"D":150,"G":90,"K":110})
st1.m1("G",130)
print(st1.m2("GD"))
print(st1.m2("KEJ"))
st1.show()


