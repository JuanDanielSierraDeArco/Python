print('-----------Metodo slice------')

# Definimos una lista de ejemplo 'lista_a'
lista_a = [1, 2, 3, 4, 5, 6, 7, 8]

# Asignamos 'lista_a' a 'lista_b', ambas referencian al mismo objeto en memoria
lista_b = lista_a

# Imprimimos las listas 'lista_a' y 'lista_b'
print(lista_a)  # Salida: [1, 2, 3, 4, 5, 6, 7, 8]
print(lista_b)  # Salida: [1, 2, 3, 4, 5, 6, 7, 8]

# Imprimimos las IDs de 'lista_a' y 'lista_b' para demostrar que son el mismo objeto
print(id(lista_a))  # Salida: ID de la lista 'lista_a'
print(id(lista_b))  # Salida: misma ID que 'lista_a'

# Creamos una copia de 'lista_a' usando el método slice
lista_c = lista_a[:]

# Creamos otra copia de 'lista_a' usando el método copy
lista_d = lista_a.copy()

# Eliminamos el primer elemento de 'lista_a'
del lista_a[0]

# Imprimimos las listas después de la modificación
print(lista_a)  # Salida: [2, 3, 4, 5, 6, 7, 8] - 'lista_a' ha sido modificada
print(lista_b)  # Salida: [2, 3, 4, 5, 6, 7, 8] - 'lista_b' también refleja la modificación
print(lista_c)  # Salida: [1, 2, 3, 4, 5, 6, 7, 8] - 'lista_c' no ha sido modificada
print(lista_d)  # Salida: [1, 2, 3, 4, 5, 6, 7, 8] - 'lista_d' no ha sido modificada

# Imprimimos las IDs de las listas para mostrar que son diferentes objetos
print(id(lista_a))  # Salida: nueva ID de la lista 'lista_a'
print(id(lista_b))  # Salida: misma ID que 'lista_a' porque 'lista_b' es solo una referencia
print(id(lista_c))  # Salida: ID diferente porque 'lista_c' es una copia
print(id(lista_d))  # Salida: ID diferente porque 'lista_d' es una copia