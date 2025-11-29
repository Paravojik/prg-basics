import queue



def rpn(expression):
    arr=queue.LifoQueue()
    for i in expression.split():
        if i.isdigit():
            arr.put(int(i))
        elif i in '+-*/':
            b=arr.get()
            a=arr.get()
            if i=='+':
                arr.put(a+b)
            elif i=='-':
                arr.put(a-b)
            elif i=='*':
                arr.put(a*b)
            elif i=='/':
                arr.put(a/b)
        elif i=='=':
            return arr.get()
exp1='2 3 + ='
exp2='2 4 1 + * ='
exp3='2 3 + 4 5 + * ='
exp4='8 3 1 + / 3 2 - 4 + * ='

print(rpn(exp1))
print(rpn(exp2))
print(rpn(exp3))
print(rpn(exp4))


