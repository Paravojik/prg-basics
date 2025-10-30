plain_text = 'The early bird catches the worm'
encrypted_text = ''
shift=4
for char in plain_text:
    if char!=" ":
        val=ord(char)+shift 
        encrypted_text+=chr(val)
    else:
        encrypted_text+=' '

print(plain_text)
print(encrypted_text)