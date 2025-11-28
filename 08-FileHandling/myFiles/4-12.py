file_path="./books.csv"
fantasy_path='./books_fantasy.txt'
historical_path='./books_historical.txt'
romance_path='./books_romance.txt'
classic_path='./books_classic.txt'
with open(fantasy_path,"w", encoding="utf-8") as fantasy_file:
    fantasy_file.write("Title,Author,Genre,Year\n")
with open(historical_path,"w", encoding="utf-8") as historical_file:
    historical_file.write("Title,Author,Genre,Year\n")
with open(romance_path,"w", encoding="utf-8") as romance_file:
    romance_file.write("Title,Author,Genre,Year\n")
with open(classic_path,"w", encoding="utf-8") as classic_file:
    classic_file.write("Title,Author,Genre,Year\n")
with open(file_path, encoding="utf-8") as file:
    content=file.readlines()
    for line in content[1:]:
        val=line.strip().split(',')
        genre=val[2].lower()
        if genre=="fantasy":
            with open(fantasy_path,"a", encoding="utf-8") as fantasy_file:
                fantasy_file.write(line)
        elif genre=="historical":
            with open(historical_path,"a", encoding="utf-8") as historical_file:
                historical_file.write(line)
        elif genre=="romance":
            with open(romance_path,"a", encoding="utf-8") as romance_file:
                romance_file.write(line)
        elif genre=="classic":
            with open(classic_path,"a", encoding="utf-8") as classic_file:
                classic_file.write(line)