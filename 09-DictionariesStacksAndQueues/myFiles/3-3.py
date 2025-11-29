import queue




a=int(input('Enter a number: '))

def toBin(a):
    arr=queue.LifoQueue()
    while a>0:
        arr.put(a%2)
        a=a//2
    return ''.join([str(arr.get()) for _ in range(arr.qsize())])
print(toBin(a))