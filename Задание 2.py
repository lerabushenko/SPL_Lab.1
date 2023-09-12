# Ввести строку текста. Вывести на экран все слова палиндромы

string = input("Введите строку: ")
string = string.lower()
words = string.split()
ammount_of_palindroms = 0
for element in words:
    word = element[::-1]
    if word == element:
        print(word)
        ammount_of_palindroms += 1
if ammount_of_palindroms == 0:
    print("В данной строке нет палиндромов")
