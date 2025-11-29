# Price list
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# Shopping cart with quantities
cart = {'juice': 3, 'bread': 1, 'milk': 2}
total=0
for i,j in cart.items():
    if i in prices:
        total+=prices[i]*j

print(f'Total price: ${total:.2f}')