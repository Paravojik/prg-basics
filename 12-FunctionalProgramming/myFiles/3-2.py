sentence="I completely agree with you"

arr=list(map(lambda x:len(x),sentence.strip().split()))
print(f"No. of letters in words: {arr}")
