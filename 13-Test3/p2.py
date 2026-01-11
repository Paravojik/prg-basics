import math

class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def m1(self):
        # Returns 0 if on axis, else quadrant 1-4
        if self.x == 0 or self.y == 0:
            return 0
        elif self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4

    def m2(self, a, b):
        # Compare quadrant of self with point (a,b)
        other_point = C(a, b)
        return self.m1() == other_point.m1()

    def m3(self, a, b):
        # Distance formula: sqrt((x2-x1)^2 + (y2-y1)^2)
        dist = math.sqrt((self.x - a)**2 + (self.y - b)**2)
        return dist > 5

if __name__ == "__main__":
    p = C(2, 3)
    print(p.m1())       # Expected: 1
    print(p.m2(7, 4))   # Expected: True
    print(p.m2(-3, 1))  # Expected: False
    print(p.m3(8, 5))   # Expected: True
    print(p.m3(4, 7))   # Expected: False

    p1 = C(0, 5)
    print(p1.m1())      # Expected: 0
    print(p1.m2(4, 7))  # Expected: False
    print(p1.m2(-7, 0)) # Expected: True