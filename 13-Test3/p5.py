import re

def f(mnumbers):
    # Pattern: Optional + or - at start
    # Followed by only characters 1-7, a, b, c, d (case insensitive)
    pattern = r"^[+-]?[1-7a-dA-D]+$"
    
    count = 0
    for num in mnumbers:
        if re.match(pattern, num):
            count += 1
    return count

if __name__ == "__main__":
    print(f(["A15", "-31", "7abc", "+D1", "-g4"]))             # Expected: 4
    print(f(["A05", "-3+1", "7ab8C", "+Bb7", "-22c55"]))       # Expected: 2