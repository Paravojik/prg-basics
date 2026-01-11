def f(uid):
    # Convert list to set to remove duplicates
    # Compare length of set to length of original list
    return len(set(uid)) == len(uid)

if __name__ == "__main__":
    print(f(["john5", "ann123", "JOHN5", "xxx", "abc333", "a10"])) # Expected: True
    print(f(["abc123", "ann", "abc123", "a10"]))                   # Expected: False