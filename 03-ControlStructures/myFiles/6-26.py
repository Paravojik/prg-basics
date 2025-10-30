PIN='1234'
isCorrect=False
for i in range(3):
    entered_pin=input("Enter your PIN: ")
    if entered_pin==PIN:
        print("PIN accepted. Access granted.")
        isCorrect=True
        break
    else:
        print("Incorrect...")
if isCorrect==False:
    print("Sorry, your payment card has been blocked.")