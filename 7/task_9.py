print('Задача 9. ...Теперь можно посчитать и свою')

# Пока бухгалтер считала среднюю зарплату сотрудников,
# ей стало интересно, а не зря ли она работает столько времени на одном месте?
# Ей захотелось узнать, увеличивается ли её зарплата с каждым месяцем или нет.
# 
# Пользователь вводит 10 чисел.
# Напишите программу, которая проверяет, упорядочены ли они по возрастанию.


# No negative numbers treatment
L_START =   1
L_END =     11         # No need to add 1 in range() 
previous_number = 0
grow = True

for counter in range(L_START, L_END):
    user_number = int(input("Введите число №"+str(counter)+":"))
    if user_number < previous_number:
        grow = False
    previous_number = user_number

if grow:
    print("Зарплата растёт")
else:
    print("Зарплата не растёт")
