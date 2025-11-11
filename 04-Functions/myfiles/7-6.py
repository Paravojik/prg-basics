def hide(card_number):
    return card_number[0:2]+"*"*10+card_number[-4:]
if __name__=="__main__":
    card=str(input("Enter card number: "))
    print(hide(card))