total_sum = 0
total_number=0
while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    total_number+=1

print(f"The total sum of the numbers is: {total_sum} and average is {round(total_sum/total_number,2)}")