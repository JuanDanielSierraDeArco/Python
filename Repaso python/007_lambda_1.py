# lambda 

add = lambda a, b: a + b
print(add(10,5))

multiply = lambda a,b:a*b
print(multiply(15,4))

#el cuadrado de los numeros de un alista
numbers = range(11)
print(list(numbers))
squared_number = list(map(lambda x: x**2,numbers))
print(squared_number)

#numeros pares de una lista
even_numbers = list(filter(lambda x: x % 2 == 0,numbers))
print(even_numbers)

#numeros impares

odd_numbers = list(filter(lambda x : x % 2 != 0, numbers))
print(odd_numbers)