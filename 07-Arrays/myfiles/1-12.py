categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]
ex=max(expenses)
ind=expenses.index(ex)
print("Highest expense category:", categories[ind])
