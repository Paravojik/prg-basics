

file_path="./powers.txt"
with open(file_path,"w") as file:
    for i in range(1,101):
        file.write(f"{i},{i**2},{i**3}\n")
        print(f"{i},{i**2},{i**3}")
