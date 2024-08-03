print("-----------listas-----\n")

# Crea una lista de números y la imprime junto con su tipo
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(type(numbers))
print()

# Crea una lista de tareas y la imprime junto con su tipo
tasks = ['order', 'wash', 'shopping']
print(tasks)
print(type(tasks))
print()

# Crea una lista con diferentes tipos de datos y la imprime junto con su tipo
types = [1, True, 'HELLO']
print(types)
print(type(types))
print()

# Imprime la lista de tareas, cambia el primer elemento y la vuelve a imprimir
print(tasks)
tasks[0] = 'watch platzi course'
print(tasks)
print()

# Imprime los primeros tres elementos de la lista de números
print(numbers[:3])
print()

# Verifica si True está en la lista 'types' y si 'HELLO' está en la lista 'types', e imprime los resultados
print(True in types)
print('HELLO' in types)

# Crea una lista mixta de números
mix = [1, 2, 3 , 4, 5, 6, 7, 8, 9, 10]

# Imprime el primer elemento de la lista 'mix'
print('Primera posicion', mix[0])

# Imprime la lista 'mix' desde la posición 5 hasta el final usando el método format para insertar la sublista en el mensaje
print('Quiero que me muestre desde la posicion 5,{}'.format(mix[5:]))

# Imprime la lista 'mix' desde el inicio hasta la posición 5 (sin incluirla) usando el método format para insertar la sublista en el mensaje
print('Quiero que me muestre antes la posicion 5,{}'.format(mix[:5]))



