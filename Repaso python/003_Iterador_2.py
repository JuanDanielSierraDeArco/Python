# ejemplo de iterador

#crear una lista
numbers = [1, 2, 3, 4]

#obtener un iterador
my_iter = iter(numbers)

#Usar el iterador
print(next(my_iter))  # Imprime 1
print(next(my_iter))  # Imprime 2
print(next(my_iter))  # Imprime 3
print(next(my_iter))  # Imprime 4
