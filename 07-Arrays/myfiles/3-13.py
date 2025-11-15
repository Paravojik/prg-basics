def occurs(number, array):
    return True if number in array else False
arr=[15, 38, 7, 23, 14]
a=int(input("Enter a number: "))
print(f'Result: number {a} {"does" if occurs(a, arr) else "does not"} appear in the array')


    