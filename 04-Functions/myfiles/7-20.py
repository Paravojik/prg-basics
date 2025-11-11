def findNPrime(n):
    primeNumbers=[]
    count=0
    curNum=1
    while count<n:
        curNum+=1
        isPrime=True
        for i in range(len(primeNumbers)):
            if primeNumbers[i]*primeNumbers[i]>curNum:
                break
            if curNum%primeNumbers[i]==0:
                isPrime=False
                break
        if isPrime:
            primeNumbers.append(curNum)
            count+=1
    return primeNumbers[-1]
if __name__=="__main__":
    n=int(input("Enter a number of prime numbers that you want to get: "))
    print(findNPrime(n))