def f(fnc, prods):
    # Apply fnc to each product
    mapped_prods = [fnc(p) for p in prods]
    # Join with comma
    return ",".join(mapped_prods)

if __name__ == "__main__":
    prods = ["water", "cheese", "tomato"]
    fnc1 = lambda x: "id:" + x[:2]
    print(f(fnc1, prods)) # Expected: "id:wa,id:ch,id:to"

    fnc2 = lambda x: (x[0] + x[-1]).upper()
    print(f(fnc2, prods)) # Expected: "WR,CE,TO"