university = 'Krakow University of Economics'
university_expanded = ''

for char in university:
    university_expanded +=char+' '

print(university) # original university name
print(university_expanded[:-1]) # expanded university name
