def detector(room):
    count=0
    for i in room:
        if i=="+":
            count+=1
            if count>=3:
                return True
        else:
            count-=1
    return False
if __name__=="__main__":
    room=str(input("Enter room layout: "))
    print(detector(room))