class Phone():
    def __init__(self,model, price=1000):
        self.model=model
        self.price=price
        self.isActive=False
    

    def displayModel(self):
        print(f'It is {self.model}')
    
    def lowerThePrice(self, percentage):
        self.price-=self.price*(percentage/100)
        print(f'Now the price of {self.model} is {round(self.price,2)}$')

    def activate(self):
        if self.isActive==False:
            self.isActive=True
            print(f'Now {self.model} is acticated')
        else:
            print(f'{self.model} has already been activated')



if __name__=="__main__":
    phone1=Phone("Iphone 16 Pro Max",price= 1200)
    phone1.displayModel()
    phone1.lowerThePrice(10)
    phone1.activate()
    phone1.activate()
    phone1.lowerThePrice(15)