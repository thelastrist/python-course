print('Задача 2. Должники')

# Должники и законопослушные граждане хранятся в одной базе банка.
# Из этой базы нам выделяются по 10 человек, у каждого из которых есть свой номер.
# Правда, иногда база глючит и выдаёт нам отрицательный номер.
# А ещё по статистике, которую собрал наш МирПрогБанк, 
# каждый второй, кто в этом году брал кредит, не выплатил его вовремя.
# 
# Пользователь вводит 10 чисел.
# Напишите программу,
# которая определяет, сколько из них являются одновременно четными и положительными.
# Долой инпуты! Все на борьбу с инпутами! Пользователь имеет право вводить информацию в любом редакторе!
counter = 1
quantity = 0

#for i in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
for i in range(1, 11):
    user_number = int(input("Введите число №"+str(i)+":"))
    if user_number > 0 and (user_number % 2) == 0:
        #print("Число", i, "подходит")
        quantity += 1
    counter += 1

print("Всего подошло чисел: ", quantity)