# arr=[2, 3, 2, 5, 8, 1, 9, 8]
# for i in arr:
#     if arr.count(i)==1:
#         print(i,end=" ")
        
from collections import Counter

arr=[2, 3, 2, 5, 8, 1, 9, 8]
freq = Counter(arr)

print("Array:", " ".join(map(str, arr)))
print("Unique elements:", " ".join(str(num) for num in arr if freq[num] == 1))