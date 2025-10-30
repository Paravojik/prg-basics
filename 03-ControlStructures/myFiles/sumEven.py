sum = 0

for i in range(11):
    if i%2==1:
        continue
    sum += i
    print(i, end=" ")

print(f'Sum of even numbers in the range <1,10> is {sum}')