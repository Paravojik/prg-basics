import random
# arr=[0 for i in range(18)]
# for i in range(1000000):
#     dice_roll_1 = random.randint(1, 6)
#     dice_roll_2 = random.randint(1, 6)
#     dice_roll_3 = random.randint(1, 6)
#     total = dice_roll_1 + dice_roll_2 + dice_roll_3
#     arr[total-1] += 1
# print(arr)
# for i in range(len(arr)):
#     print(f'Percentage {i+1}: {arr[i]/1000000*100}%')




dice_roll_1 = random.randint(1, 6)
dice_roll_2 = random.randint(1, 6)
dice_roll_3 = random.randint(1, 6)
total = dice_roll_1 + dice_roll_2 + dice_roll_3
print(f'Dice rolled: {total}')  
