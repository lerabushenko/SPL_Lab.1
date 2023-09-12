# 5.	Реализуйте программу «Ювелирный магазин», которая будет включать
# в себя шесть пунктов меню.  У вас есть словарь, где ключ – название изделия.
# Значение – список, который содержит состав изделия(золото, серебро,и т.п.),
# цену и кол-во (шт),которое есть в магазине.
# 1.	Просмотр описания: название – описание
# 2.	Просмотр цены: название – цена.
# 3.	Просмотр количества: название – количество.
# 4.	Всю информацию.
# 5.	Покупка
# В пункте «Покупка» необходимо совершить покупку,  с клавиатуры вводите название изделия
# и его кол-во, n – выход из программы. Посчитать цену выбранных товаров и сколько товаров
# осталось в изначальном списке.
# 6.	До свидания

dictionary = {
    "Кольцо": ["Золото", 350, 23],
    "Колье": ["Бриллианты", 520, 14],
    "Серьги": ["Серебро", 112, 4]
}
list_item = []
list_cost = []
cost = 0
while 1:
    print("Меню")
    print("1 - просмотреть описание")
    print("2 - просмотреть цену")
    print("3 - просмотреть количество")
    print("4 - просмотреть всю информацию")
    print("5 - купить")
    print("0 - выход")
    choice = int(input("Ваш выбор: "))
    if choice == 1:
        for item in dictionary:
            print(item, dictionary[item][0])
    elif choice == 2:
        for item in dictionary:
            print(item, dictionary[item][1])
    elif choice == 3:
        for item in dictionary:
            print(item, dictionary[item][2])
    elif choice == 4:
        print(dictionary.items())
    elif choice == 5:
        while 1:
            jewelry = input("Введите название украшения, которое хотите приобрести (n - выход): ")
            if jewelry == "n":
                if cost == 0:
                    print("Вы ничего не приобрели(((")
                else:
                    dict_purchase = dict(zip(list_item, list_cost))
                    print(dict_purchase.items())
                    print("Итоговая сумма покупки: ", cost)
                break
            is_find = 0
            for item in dictionary:
                if item == jewelry:
                    ammount = int(input("Введите количество украшений: "))
                    if ammount > dictionary[item][2]:
                        print("В магазине нет необходимого количества украшений")
                    else:
                        cost += dictionary[item][1] * ammount
                        list_item.append(item)
                        list_cost.append([dictionary[item][1], ammount])
                        dictionary[item][2] -= ammount
                        is_find = 1
                        print("Товар добавлен в корзину")
            if is_find == 0:
                print("Такого товара не найдено")
    elif choice == 0:
        print("Хорошего дня! Приходите ещё!))")
        break
    else:
        print("Введено неверное значение")
