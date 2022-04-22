print('Задача 10. Максимальное число (по желанию)')

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно 
iDigit1 = int(input("Введите первое число: "))
iDigit2 = int(input("Введите второе число: "))
iDigit3 = int(input("Введите третье число: "))

if iDigit1 > iDigit2:
 if iDigit1 > iDigit3:
  max = iDigit1
 else:
  max = iDigit3
else:
 if iDigit2 > iDigit3:
  max = iDigit2
 else:
  max = iDigit3
          
print("Max:", max)


