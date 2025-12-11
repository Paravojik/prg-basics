people=[
    {"name":"John", "age":24},
    {"name":"Ann", "age":19},
    {"name":"Peter", "age":31}
]
# print(people[0]["name"])
print(people)

ps=sorted(people, key=lambda x:x["age"],reverse=True)


print(ps)