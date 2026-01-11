def f(d):
    if not d:
        return 0
        
    passengers = list(d.values())
    avg = sum(passengers) / len(passengers)
    
    count = 0
    for num in passengers:
        if num > avg:
            count += 1
            
    return count

if __name__ == "__main__":
    print(f({"LO231": 150, "BA787": 120, "NZ15": 30})) # Expected: 2 
    print(f({"LO231": 150, "BA787": 20, "NZ15": 30}))  # Expected: 1