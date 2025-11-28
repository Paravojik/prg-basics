import re
a=str(input("Enter some text: \n"))
amountOfVowels=re.findall(r"[aeouiyAEIOUY]",a)
print(f"Amount of vowels: {len(amountOfVowels)}")
