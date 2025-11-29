price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
def showProducts(prices):
    for product, price in prices.items():
        print(f"{product}: ${round(price,2)}")

def totalValue(prices):
    total=0
    for i in prices.values():
        total+=i
    return round(total,2)

def applyDiscount(prices):
    for i,j in prices.items():
        prices[i]=round(j*0.9,2)
    return prices





showProducts(price_list)
print(f'${totalValue(price_list)}')
discounted_prices = applyDiscount(price_list)
showProducts(discounted_prices)
print(f'${totalValue(discounted_prices)}')