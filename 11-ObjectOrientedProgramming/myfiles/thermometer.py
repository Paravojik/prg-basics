import random
class Thermometer:
    def __init__(self):
        self.is_on=False

    def toogle_on(self):
        self.is_on=not self.is_on
    

    def measure(self):
        if self.is_on:
            self.temperature=round(random.random()*8+34,1)
        else:
            print(f"It is turned off")

    def display_temp(self):
        if self.temperature>41:
            print(f"Temperature: {self.temperature}C (CRITICAL TEMPERATURE!!)")
        elif self.temperature>37:
            print(f"Temperature: {self.temperature}C (fever)")
        else:
            print(f"Temperature: {self.temperature}C")




