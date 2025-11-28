import re 

email_file = 'report.txt'

def extract_emails(fileName):
    with open(fileName, "r", encoding="utf-8") as file:
        return file.read()
    
content = extract_emails(email_file)
amount=re.findall(r'€\d+',content)
print(sum(int(i[1:]) for i in amount))