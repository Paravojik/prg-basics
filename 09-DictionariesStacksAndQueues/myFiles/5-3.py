translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}

a=str(input('Enther the word to translate: '))
if a in translations:
    print(translations[a])
else:
    print('There is no such word')
