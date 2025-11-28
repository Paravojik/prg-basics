import re
file_path="./email.txt"
with open(file_path,"r", encoding="utf-8") as file:
    emails=file.read()

# print(emails)
def senderEmail(email):
    pattern=r"From:\s*(.*)"
    match=re.search(pattern,email)
    if match:
        return match.group(1)
    else:
        return None
def emailRecipient(email):
    pattern=r"To:\s*(.*)"
    match=re.search(pattern,email)
    if match:
        return match.group(1)
    else:
        return None
def emailSubject(email):
    pattern=r'Subject:\s(.*)'
    match=re.search(pattern,email)
    if match:
        return match.group(1)
    return None 
def emailBody(email):

    pattern=r"\n\n(.*)" 
    match=re.search(pattern, email, re.DOTALL)
    if match:
        return match.group(1)
    return None
print(f"Sender: {senderEmail(emails)}")
print(f"Recipient: {emailRecipient(emails)}")
print(f"Subject: {emailSubject(emails)}")
print(f"Body: {emailBody(emails)}")