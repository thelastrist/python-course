print('Задача 9. Выражение')


#Дано число x.
#Напишите программу для вычисления следующего выражения 

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64)) 
x = float(input("Enter x: "))
divisible, divisor, quotient = 1, 1, 0
#print(2**6)
for i in range(1, 7):
    divisible *= x - (i ** 2 - 1)
    divisor *= x - i ** 2
    print(divisible, divisor)
    
quotient = divisible / divisor
print("Result =", quotient)
