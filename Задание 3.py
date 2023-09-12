# 3.Найдите произведение элементов списка с нечетными номерами.
# Найдите наибольший элемент списка, затем удалите его и выведите новый список.
# Выведите на экран три наибольших элемента.

import random
size = int(input("Введите размер списка: "))
list1 = [random.randint(-50, 50) for i in range(size)]
proizv = 1
for i in range(0, size, 2):
    proizv *= list1[i]
print("Список: ", list1)
print("Произведение элементов с нечетными номерами: ", proizv)

print("Максимальный элемент списка: ", max(list1))
list1.remove(max(list1))
print("Новый список: ", list1)

print("Три наибольших элемента: ")
for i in range(3):
    print(max(list1))
    list1.remove(max(list1))
