print('Задача 9. Выражение')


#Дано число x.
#Напишите программу для вычисления следующего выражения 

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64)) 
x = float(input("Enter x: "))
divisible, divisor, quotient = x - 1, x - 2, 0
#print(2**6)
for i in range(2, 7):
    divisible *= x - (2 ** i - 1)
    divisor *= x - 2 ** i
#    mixed up 2**i with i**2
    
quotient = divisible / divisor
print("Result =", quotient)
