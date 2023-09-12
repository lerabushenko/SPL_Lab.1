# Вычислите сумму цифр введенного натурального числа

number = int(input("Введите натуральное число: "))
summa = 0
while number != 0:
    summa += number % 10
    number //= 10
print("Сумма цифр числа: ", summa)
