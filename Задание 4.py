# 4. Даны два списка одинаковой длины.
# Необходимо создать из них словарь таким образом,
# чтобы элементы первого списка были ключами,
# а элементы второго — соответственно значениями нашего словаря.

size = int(input("Введите размер списков: "))
print("Введите первый список: ")
list1 = []
for i in range(size):
    list1.append(input())
print("Введите второй список: ")
list2 = []
for i in range(size):
    list2.append(input())
dictionary = dict()
for i in range(size):
    dictionary[list1[i]] = list2[i]

# dictionary = dict(zip(list1, list2))

print(dictionary.items())
