speeds=[48,47,54,50,42,68,39,46]

h_speeds=list(filter(lambda x:x>50,speeds))
h_speeds=list(map(lambda x:str(x),h_speeds))
print("Speed to high:", ",".join(h_speeds))
