file_path="./it_company.csv"


with open(file_path,"r") as file:
    companies=file.readlines()
count=0
for company in companies[1:]:
    print(company,end="")
    count+=1
    if count%5==0:
        input("Enter to continue...")
