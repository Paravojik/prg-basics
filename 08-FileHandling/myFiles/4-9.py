import csv
print("GRAPHIC DESIGNERS")
print("------------------")
with open('./it_company.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if row[2]=="Graphic Designer":
            print(row[0], row[1], row[3])

