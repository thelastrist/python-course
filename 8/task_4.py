print('Задача 4. Отрезок')

#Напишите программу, 
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль среднее арифметическое
# всех чисел из отрезка [a; b], которые кратны числу c.
# Подсказка: (a и b  являются промежутком, а c для проверки кратности).
number_a = int(input("Введите число a: "))
number_b = int(input("Введите число b: "))
number_c = int(input("Введите число c: "))

average, counter = 0, 0


for i in range(number_a, number_b + 1, number_c):
    if i % number_c == 0:
        counter += 1
        average += i

print("Average is", average / counter)