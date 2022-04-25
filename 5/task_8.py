print('Задача 8. Новоселье')

# Семья из трёх человек устала тесниться в однушке и наконец решила переехать.
# При обсуждении,
# какую же всё-таки купить квартиру исходя из своих предпочтений и семейного бюджета,
# они остановились на нескольких вариантах:

# Первый вариант 
# они готовы взять квартиру попросторнее (не менее 100 квадратных метров),
# но стоимостью не более 10 млн.
 
# Второй вариант — немного расширить круг поиска,
# то есть взять квартиру поменьше (от 80 квадратный метров),
# но и стоимостью не более 7 млн.
 
# Напишите программу,
# которая получает на вход стоимость квартиры и её площадь
# и выводит сообщение о том, подходит она или нет
iPrice = int(input("Введите цену квартиры: "))
iAcreage = int(input("Введите площадь квартиры: "))

if (iPrice <= 10 and iAcreage >= 100) or (iPrice <= 7 and iAcreage >= 80):
 print ("Подходит, цена за квадрат ", iPrice * 1000000 / iAcreage)
else:
 print ("Не подходит, цена за квадрат ", iPrice * 1000000 / iAcreage)