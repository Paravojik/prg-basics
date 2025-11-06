def pts_to_grade(grade):
    if grade>=18:
        return "Excelent"
    elif grade>=14:
        return "Good"
    elif grade>=10:
        return "Satisfactory"
    else:
        return "Fail"



a=int(input("Enter your grade: "))
final_grade=pts_to_grade(a)
print(f"You scored {a} points on the test. Your final grade is {final_grade}")