import re

file_path="./files.txt"


with open(file_path,"r", encoding="utf-8") as file:
    content=file.read()

myFiles= re.findall(r'.*\.\w{4}',content)
for i in myFiles:
    print(i)