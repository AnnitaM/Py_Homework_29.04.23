# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
#
# Input:
# 1
# 2
# 5
# Output:
# 1, 3, 5, 7, 9


start = int(input("Enter first element of the progression "))
dffrnc = int(input("Enter the progression difference "))
number = int(input("Enter the element number "))
result = []
for i in range(start, number+1):
    result.append(start + (i-1)* dffrnc)
print(result)

# def a_progression(start, dffrnc, number):
#     result = []
#     for i in range(number+1):
#         result.append(start + (i-1) + dffrnc)
#     return print(result)
