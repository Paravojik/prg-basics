def IsPalindrome(s):
    return s==s[::-1]
if __name__=="__main__":
    text=str(input("Enter a text: "))
    print(IsPalindrome(text))