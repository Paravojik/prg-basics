def isInRange(num, start, end):
    return start <= num <= end
a=int(input("Enter a number: "))
x=int(input("Enter range start: "))
y=int(input("Enter range end: "))
print(f'Number {a} in the range <{x},{y}>: {"yes" if isInRange(a, x, y) else "no"}')