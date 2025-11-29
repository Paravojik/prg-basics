import queue

arr=queue.LifoQueue()
arr.put(2)
arr.put(3)
arr.put(7)
arr.put(4)
arr.put(1)
arr.put(9)
arr.put(8)
print(arr.get()+arr.get())
print('as')
tot=0
while not arr.empty():
    tot += arr.get()
print("Total:", tot)