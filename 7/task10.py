print('Задача 10.')

#Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.
# 
# Вводится число N,
# далее еще N − 1 чисел: 
# номера оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.

cards_quantity = int(input("Введите количество карточек: "))
#cards_quantity += 1 # for range
sum, sum_all = 0, cards_quantity

for counter in range(1, cards_quantity):
    user_number = int(input("Введите число №"+str(counter)+":"))
    sum += user_number
    sum_all += counter



print("Пропала карточка №", sum_all - sum)
