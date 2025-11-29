countries = [
{"name":"Poland", "population":38000000},
    {"name":"Germany", "population":83000000},
    {"name":"France", "population":67000000},
    {"name":"Italy", "population":60000000},
    {"name":"Ukraine", "population":41000000}
]
arr=[len('Country')]
for i in countries:
    arr+=[len(i["name"])]
m=max(arr)
print(f"{'COUNTRY':<{m}} {'POPULATION':<15}")
for country in countries:
    print(f"{country['name']:<{m}} {country['population']:<15}")