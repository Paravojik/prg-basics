def removeSpaces(text):
    return "".join(text.split())
if __name__=="__main__":
    txt=str(input("Enter a text: "))
    print(removeSpaces(txt))