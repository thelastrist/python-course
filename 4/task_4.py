print('Задача 4. Калькулятор скидки')

# Андрей переехал на новую квартиру, и ему нужно купить три стула в разные комнаты.
# Естественно, цена на стулья в разных магазинах различается,
# а где-то ещё и скидка есть. 
# Вот для одного из таких магазинов он и написал калькулятор скидки, 
# чтобы проще ориентироваться в ценах.
 
# Напишите программу,
# которая запрашивает три стоимости товара и вычисляет сумму чека. 
# Если сумма чека превышает 10 000 рублей,
# то нужно вычесть из этой суммы скидку 10% (умножить на 10, разделить на 100). 
# В конце вывести итоговую сумму на экран.
iPrice1 = int(input("Введите цену первого стула:"))
iPrice2 = int(input("Введите цену второго стула:"))
iPrice3 = int(input("Введите цену третьего стула:"))
sum = iPrice1 + iPrice2 + iPrice3
if (sum) > 10000:
    print("Поздравляю, скидка", sum / 10, "всего нужно заплатить", sum - sum / 10)
else:
    print("К сожалению скидки не будет, сумма", sum)
