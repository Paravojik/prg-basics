def numberOfCoins(amount):
    count=0
    count+=amount//5
    amount=amount%5
    count+=amount//2
    amount=amount%2
    count+=amount
    return count
if __name__=="__main__":
    a=int(input("Enter amount in PLN: "))
    print(f'Minimum number of coins for {a} PLN is {numberOfCoins(a)}')