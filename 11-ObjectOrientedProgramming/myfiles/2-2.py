class Square:
   def __init__(self, a):
      self.a = a
   def area(self):
      return self.a * self.a
   def perimeter(self):
      return self.a*4
   

if __name__=="__main__":
    square1=Square(4)
    square2=Square(6)


    print(f'Square with side {square1.a}: ')
    print(f'Area is {square1.area()} and Perimeter is {square1.perimeter()}\n')
    print(f'Square with side {square2.a}: ')
    print(f'Area is {square2.area()} and Perimeter is {square2.perimeter()}')
