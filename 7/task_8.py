print('Задача 8. Замечательные числа')

#Напишите программу,
# которая находит и выводит все двузначные числа,
# которые равны утроенному произведению своих цифр.
# К таким относятся, например, 15 и 24.

L_START = 10
L_END = 100         # No need to add 1 in range() 

counter, quantity, sum = 0, 0, 0
medium, digit_dec, digit_sec = 0, 0, 0

for counter in range(L_START, L_END):
    #user_number = int(input("Введите число №"+str(i)+":"))
    digit_dec = counter // 10
    digit_sec = counter % 10
    
    if (digit_sec * digit_dec * 3) == counter:
        sum += counter
        quantity += 1
        print("Хитрое число: ", counter)


print("Хитрых чисел: ", quantity)



""" number_a = int(input("Введите число a: "))
number_b = int(input("Введите число b: "))
if number_a > number_b:
    sum = number_a
    number_a = number_b
    number_b = sum

sum = 0

 """