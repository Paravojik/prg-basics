def acronim(phrase):
    words=phrase.split()
    ans=""
    for i in words:
        ans+=i[0]
    return ans
if __name__=="__main__":
    text=str(input("Enter a phrase: "))
    print(acronim(text))