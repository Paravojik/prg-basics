
import re
file_path="./"+str(input("Enter file name: "))

try:
    with open(file_path,"r", encoding="utf-8") as file:
        content=file.read()
        print(content)

except FileNotFoundError:
    print("File not found. Please check the file name and try again.")

numLines=re.findall(r'\n',content)
print(f"Number of lines: {len(numLines)+1}")
# numWords=re.findall(r'([\s\n,\:;]+)',content)
numWords=re.findall(r'(\s+)',content)
numCharachters=re.findall(r'\w',content)
print(f"Number of words: {len(numWords)}")
print(f"Number of characters: {len(numCharachters)}")