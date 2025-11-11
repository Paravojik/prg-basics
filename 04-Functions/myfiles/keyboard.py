def input_string(message):
    ans = input(message)
    return ans

def input_integer(message):
    ans = int(input(message))
    return ans

def input_real(message):
    ans = float(input(message))
    return ans

def input_boolean(message):
    ans = input(message)
    if ans.lower()=='y':
        ans=True
    elif ans.lower()=='n':
        ans=False
    return ans