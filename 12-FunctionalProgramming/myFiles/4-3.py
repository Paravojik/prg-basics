grades=[3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]
positiveGrades=list(filter(lambda x:x>2,grades))
print(positiveGrades)
print("Arithmetic mean for grades <> 2.0 is", round(sum(positiveGrades)/len(positiveGrades),2))