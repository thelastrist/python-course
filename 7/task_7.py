print('Задача 7. Отрезок')

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль 
#среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.

counter, quantity, sum = 0, 0, 0
medium, number_a, number_b = 0, 0, 0

number_a = int(input("Введите число a: "))
number_b = int(input("Введите число b: "))
if number_a > number_b:
    sum = number_a
    number_a = number_b
    number_b = sum

sum = 0
number_b += 1

for counter in range(number_a, number_b):
    #user_number = int(input("Введите число №"+str(i)+":"))
    if (counter % 3) == 0 and counter != 0:
        sum += counter
        quantity += 1
    
medium = sum / quantity
print("Среднее: ", medium, "сумма: ", sum, "количество кратных трём:", quantity)
