def f(car, order):
    # car is a list of dictionaries like [{"KR333":138}, ...]
    
    # Helper to get the single item from the dictionary
    def get_item(d):
        return list(d.items())[0]

    if order == 1:
        # Sort alphabetically by registration number (the key)
        return sorted(car, key=lambda x: get_item(x)[0])
    elif order == 2:
        # Sort by km (the value) in descending order
        return sorted(car, key=lambda x: get_item(x)[1], reverse=True)

if __name__ == "__main__":
    cars = [{"KR333": 138}, {"WL555": 497}, {"DB444": 341}, {"MC222": 412}]
    print(f(cars, 1)) # Expected: sorted by key (DB..., KR..., MC..., WL...)
    print(f(cars, 2)) # Expected: sorted by value desc (WL(497), MC(412), DB(341), KR(138))