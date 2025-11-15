meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

# Returns a week day name
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n-1]

def day_meal_plan(meal_plan, day_number):
    print(f'{weekday(day_number)}: {", ".join(meal_plan[day_number-1])}')
print('WEEKLY MEAL PLAN')
print("(Breakfast, Lunch, Dinner)")
print('--------------------------')
for day in range(1, 8):
    day_meal_plan(meal_plan, day)