class Statistics:
    def __init__(self):
        self.arr=[]

    def show_numbers(self):
        print(f"All of the numbers: {" ".join(str(i) for i in self.arr)}")


    def add_number(self,num):
        self.arr.append(num)
    

    def greatest_number(self):
        print(f"The greates number is {max(self.arr)}")

    def smallest_number(self):
        print(f"The smallest number is {min(self.arr)}")
        
    def mean_numbers(self):
        print(f"The arithmetic mean is {sum(self.arr)/len(self.arr):.2f}")
    
    def median_numbers(self):
        self.arr.sort()
        if len(self.arr)%2==1:
            print(f"The median is {self.arr[len(self.arr)//2]}")
        else:
            print(f"The median is {(self.arr[len(self.arr)//2]+self.arr[len(self.arr)//2-1])/2:.2f}")

    def print_all(self):
        print()
        print(f"All of the statistics: ")
        self.greatest_number()
        self.smallest_number()
        self.mean_numbers()
        self.median_numbers()
    
