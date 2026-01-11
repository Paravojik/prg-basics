class C:
    def __init__(self, initial_value):
        self.value = initial_value

    def m1(self):
        return self.value

    def m2(self):
        self.value += 1

    def m3(self):
        self.value -= 1

    def m4(self, n):
        self.value += n

    def __str__(self):
        return str(self.value)

if __name__ == "__main__":
    c = C(5)
    print(c.m1())   # Expected: 5
    c.m2()
    print(c.m1())   # Expected: 6
    c.m4(-8)
    print(c.m1())   # Expected: -2
    c.m3()
    print(c.m1())   # Expected: -3
    c.m4(10)
    print(c.m1())   # Expected: 7
    print(c._str()) # Expected: "7"