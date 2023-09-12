# 6.	Создайте кортеж из случайных 10 чисел.
# Найдите его максимальный минимальный элемент

import random
numbers = tuple(random.randint(-50, 50) for i in range(10))
print("Кортеж: ", numbers)
print("Максимальное значение: ", max(numbers))
print("Минимальное значение: ", min(numbers))
