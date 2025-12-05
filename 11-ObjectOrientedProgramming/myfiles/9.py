class C:
    def __init__(self,name,surname,age,seniority):
        self.name=name
        self.surname=surname
        self.age=age
        self.seniority=seniority
    
    def display(self):
        val=''
        if self.age<18:
            val+=self.surname.lower()
            val+=self.name.lower()[0]
            val+=str(self.seniority)
        else:
            val+=self.surname.upper()
            val+=self.name.upper()[0]
            val+=str(self.seniority)
        return val



w1=C("Anna","May",17,7)
print(w1.display())

w2=C("George","Brown",21,4)
print(w2.display())