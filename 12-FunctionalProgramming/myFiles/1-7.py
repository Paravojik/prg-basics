a=int(input("Enter a number: "))


is_even=lambda number: "Yes" if number%2==0 else "No"

res=is_even(a)


print(f"{a} is even: {res}")