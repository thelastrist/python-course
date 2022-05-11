print('Задача 7. Стипендия')

#Ежемесячная стипендия студента составляет educational_grant руб.,
# а расходы на проживание превышают стипендию и составляют expenses руб. в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
# 
# Составьте программу расчета суммы денег,
# которую необходимо получить у родителей один раз в начале обучения,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
educational_grant = 40 # int(input("Enter educational grant: "))
expenses = 310 # int(input("Enter educational grant: "))
price_growth = .03
months = 10
parents_request = expenses - educational_grant

if expenses < educational_grant:
    print("Invalid user, replace and restart")
    exit(404)

for i in range(1, months):
     parents_request += (expenses + expenses * i * price_growth) - educational_grant
#     print(expenses * i * price_growth - educational_grant)


print("Hello parents, send me please", parents_request)
