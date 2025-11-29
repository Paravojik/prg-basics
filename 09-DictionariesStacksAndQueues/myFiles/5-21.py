import json

book_data={
    'name': '1984',
    'author': 'George Orwell',
    'year': 1949,
    'genres': ['Dystopian', 'Political Fiction', 'Social Science Fiction'],
    'available': True
}

book_path='./favourite.json'
with open(book_path,'w',encoding='utf-8') as file:
    json.dump(book_data,file,indent=2)