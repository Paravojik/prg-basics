

with open('./clothing.csv') as file:
    content=file.readlines()
    for line in content[1:]:
        val=line.strip().split(',')
        if float(val[-2])<60 and float(val[-1])<40:
            print(' '.join(val))