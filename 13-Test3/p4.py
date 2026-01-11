def f(fnc, res):
    # Filter the results based on the function fnc
    filtered_res = [x for x in res if fnc(x)]
    
    if not filtered_res:
        return 0
        
    # Return difference between highest and lowest
    return max(filtered_res) - min(filtered_res)

if __name__ == "__main__":
    res = [95, 90, 20, 50, 70]
    fnc1 = lambda x: x > 50
    print(f(fnc1, res)) # Expected: 25 

    fnc2 = lambda x: x > 30 and x < 90
    print(f(fnc2, res)) # Expected: 20