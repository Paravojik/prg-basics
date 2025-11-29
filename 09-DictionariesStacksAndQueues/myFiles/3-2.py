import queue



def checkBrackets(expression):
    arr=queue.LifoQueue()   
    for i in expression:
        if i in '([{':
            arr.put({'(':')','[':']','{':'}'}[i])
        elif i in ')]}':
            if arr.empty():
                return False
            elif arr.get() ==i:
                continue
            else:
                return False
    if arr.empty():
        return True
    else:
        return False



expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"
print(checkBrackets(expression1))
print(checkBrackets(expression2))
print(checkBrackets(expression3))

