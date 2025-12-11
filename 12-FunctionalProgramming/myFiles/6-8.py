arr=[37,51,44,23,78,92,39,84,83,51]

def whoPassed(minScore):
    print(f"Min {minScore} pts: {list(filter(lambda x:x>minScore,arr))}")

whoPassed(70)
whoPassed(40)
whoPassed(30)