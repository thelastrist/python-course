print('Задача 1. Тайны археологии')

# Ирина работает археологом и недавно приехала с интересных раскопок.
# Там нашли древнюю глиняную табличку, на которой еле-еле видны числа 
# 114 12 14 10605 4907 450. 

# Ирина предположила, что это такой шифр и хочет использовать программу,
# которую использовали для расшифровки целой книги из таких чисел.
# 
# Напишите программу,
# которая проверяет каждое число и выводит к каждому соответствующее сообщение.
# Число подходит, если оно чётное и не делится на 3.


for i in (114, 12, 14, 10605, 4907, 450):
    if (i % 3) == 0 and (i % 2) == 0:
        print("Число", i, "подходит")
    else:
        print("Число", i, "не подходит")