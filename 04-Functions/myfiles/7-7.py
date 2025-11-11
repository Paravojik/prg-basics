def isBinary(val):
    for char in val:
        if char not in ['0','1']:
            return False
    return True 

if __name__=="__main__":
    a=str(input("Enter a binary digit : "))
    print(f'The value "{a}" is binary: {"yes" if isBinary(a) else "no"}')