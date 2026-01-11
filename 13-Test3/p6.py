class C:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        initials = self.first_name[0] + self.last_name[0]
        
        if self.age < 18:
            result = initials.lower() + str(self.age)
        else:
            result = initials.upper() + str(self.age)
            
        return result

if __name__ == "__main__":
    print(C("John", "May", 21))    # Expected: JM21
    print(C("Anna", "Brown", 17))  # Expected: ab17