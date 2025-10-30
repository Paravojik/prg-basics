print("SURVEY")
fquestion="Yes" if input("Are you interested in computer science?(y/n): ")=='y'  else "No"
squestion="Yes" if input("Do you like playing computer games? (y/n): ")=='y'  else "No" 
tquestion="Yes" if input("Do you have an Instagram account? (y/n): ")=='y'  else "No" 
print("Survey results".capitalize())
print(f"Interested in computer science: {fquestion}")
print(f"Playing computer games: {squestion}")
print(f"Has an Instagram account: {tquestion}")