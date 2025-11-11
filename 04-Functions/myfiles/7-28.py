def roll(combination):
    value=combination[0]
    count=0
    max_count=0
    max_value=value
    for i in combination:
        if i==value:
            count+=1
        else:
            if count>max_count:
                max_count=count
                max_value=value
            count=1
            value=i
        if count>max_count:
            max_count=count
            max_value=value

    return max_value
if __name__ == "__main__":
    comb=str(input("Enter the combination: "))
    print(roll(comb))