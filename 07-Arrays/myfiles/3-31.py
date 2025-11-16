# arr=[[-38, 19], [5,40],[-7,11],[29,16]]

# min_val=float('inf')
# min_ind=[-1,-1]
# max_val=-float('inf')
# max_ind=[-1,-1]
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[i][j]<min_val:
#             min_val=arr[i][j]
#             min_ind=[i,j]
#         if arr[i][j]>max_val:
#             max_val=arr[i][j]
#             max_ind=[i,j]
# print(f"Min value: {min_val} at index ({", ".join(map(str, min_ind))})")
# print(f"Max value: {max_val} at index ({", ".join(map(str, max_ind))})")

arr=[[-38, 19], [5,40],[-7,11],[29,16]]

# Flatten array with positions
flat = [(arr[i][j], i, j) for i in range(len(arr)) for j in range(len(arr[i]))]

# Find min and max
min_item = min(flat, key=lambda x: x[0])
max_item = max(flat, key=lambda x: x[0])

print(f"Smallest value: {min_item[0]} at row {min_item[1]}, column {min_item[2]}")
print(f"Largest value: {max_item[0]} at row {max_item[1]}, column {max_item[2]}")