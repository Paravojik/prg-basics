bottle_capacity=500
filling_tolerance=2
bottles=[508,500,512,499,492,511,503,476,501,509,500]

def is_okay(val):
    highestPoint=bottle_capacity+bottle_capacity*filling_tolerance/100
    minimalPoint=bottle_capacity-bottle_capacity*filling_tolerance/100
    if minimalPoint<val<highestPoint:
        return True
    else:
        return False



filtered_botles=list(filter(lambda x:is_okay(x),bottles))
incorectPercentage=(len(bottles)-len(filtered_botles))/len(bottles)*100

print(f"{'Bottle capacity:':<20}{bottle_capacity}ml")
print(f"{'Filling tolerance:':<20}{filling_tolerance}%")
print(f"{'Filled bottles:':<20}{','.join(map(str,bottles))}ml")

print(f"{'Incorrectly filled:':<20}{incorectPercentage:.2f}%")
