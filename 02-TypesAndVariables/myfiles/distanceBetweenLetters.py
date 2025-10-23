first = input('Enter first letter: ')
last = input('Enter last letter: ')
distance =  abs(ord(last) - ord(first))-1 if abs(ord(last) - ord(first))!=0 else 0
print(f'Between {first} and {last} is {distance} letters')