print('Задача 9. Плохой циферблат')

# У Саши в грузовике стоит суперсовременный цифровой циферблат для подсчёта пробега,
# но он постоянно глючит и сбрасывается.
# Саша заметил закономерность:
# каждый раз, когда сумма цифр на циферблате превышает число текущего дня,
# циферблат сбрасывается.
 
# Напишите программу,
# которая получает на вход от пользователя два числа: пробег и номер дня (первое — обязательно трёхзначное),
# затем находит сумму цифр первого числа,
# и если эта сумма больше второго числа,
# выводит сообщение: «Сброс», — и сбрасывает пробег до нуля.
# В противном случае выводится: «Сегодня не сломался».
# В конце также выводится сам пробег.
kms = int(input("Введите пробег (трёхзначное число): "))
day = int(input("Введите номер дня: "))

# 234  2 23  
digits_sum = kms // 100 + (kms // 10 - (kms // 100) * 10) + kms % 10
#print(digits_sum)
if digits_sum == day:
 kms = 0
 print("Сброс")
else:
 print("Сегодня не сломался")

