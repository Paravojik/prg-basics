shopping_list = './shopping_list.txt'


def add_item(fileName,item):
    with open(fileName,"a") as file:
        file.write(item + "\n")

print("You can add items. To stop enter 0.")
while True:
    a=input("Enter item: ")
    if a=="0":
        break
    else:
        add_item(shopping_list,a)
