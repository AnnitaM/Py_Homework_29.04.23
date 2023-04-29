#  Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
#  (т.е. не меньше заданного минимума и не больше заданного максимума)
# Input:
# 1, 3, 7, 10, 5, 8
# 4
# 8
# Output:
# 2(7), 4(5), 5(8)

import random

start = int(input("Enter minimum "))
finish = int(input("Enter maximum "))
lnght = int(input("Enter array lenght "))
array = [random.randint(-10, 10) for _ in range(lnght)]
print(array)

index = []
for i in array:
    if i >= start and i <= finish:

        index.append(array.index(i))

print(index)

# index = array.index(item)