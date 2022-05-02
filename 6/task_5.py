
print('Задача 5. Счастливый билетик')

# В старину, когда даже в столице билеты в общественном транспорте выдавали контролёры,
# существовало поверье:
# если на билете сумма первых трёх цифр в номере билета равна сумме последних трёх,
# то это к удаче.
#
# Напишите программу,
# которая получала бы на входе шестизначный номер билета
# и выводила, счастливый это билет или нет.
# К примеру, билеты 666 666 и 252 135 — счастливые,
# а 123 456 — нет.
# Подумайте, нужны ли для решения этой задачи циклы?
# Долой инпуты! Времяжорки!
number = int(input("Введите число: "))
iFirst, iSecond, iSum1, iSum2 = 0, 0, 0, 0
count = 1

#555663
# get last digit (number % 10)
  # 3
# get last-1 digit (number % 100) - prev - (number // 10)
  # 63  - 3 (60) - () (brain breaked)
  # let's try func
""" def get_digit(from_one, which_one):
  digit = from_one
  return digit
 """
 # no

 
while count < 7:
    if count < 4:
        iFirst = number % 10
        number //= 10
        iSum1 += iFirst
 #       iFirst = number % (10 ** count) - iSum1
 #       iSum1 += number % (10 ** count) - iSum1
    else:
        iSecond = number % 10
        number //= 10
        iSum2 += iSecond
#
#    print(count, iFirst, iSecond, iSum1, iSum2)
    count += 1



#if sum_left == sum_right:
if iSum1 == iSum2:
    print('Билет счастливый!')
else:
    print('Неудачный билет!')




""" if ((number // 100000 > 0) and (number // 100000 < 10)):
# divide by 2 parts
 iFirst = number // 1000
 iSecond = number % 1000

 iSum1 = iFirst // 100 + (iFirst // 10 - (iFirst  // 100 * 10)) + iFirst % 10
 iSum2 = iSecond // 100 + (iSecond // 10 - (iSecond  // 100 * 10)) + iSecond % 10
 if iSum1 == iSum2:
  print("Скорее кушать этот билет, он счастливый!")


else:
 print ("Должно быть 6 цифры в билете. Ваш билет ненастоящий, вы оштрафованы на ", number, "рублей") """

#print(number // 1000000, number // 100000, number // 10000, iFirst, iSecond, iSum1, iSum2)
