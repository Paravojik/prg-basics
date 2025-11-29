import queue


def reverseString(string):
    arr=queue.LifoQueue()
    for  i in string:
        arr.put(i)
    reversed_string=''
    while not arr.empty():
        reversed_string+=arr.get()
    return reversed_string


string1 = "Hello, World!"
print(reverseString(string1)) 