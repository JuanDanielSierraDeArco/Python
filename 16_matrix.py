print('----------matrix------')

# Definimos una matriz (lista de listas) de 3x3
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Imprimimos la matriz completa
print(matrix)  # Salida: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Imprimimos la segunda fila de la matriz
print(matrix[1])  # Salida: [4, 5, 6]

# Imprimimos el elemento en la segunda fila y segunda columna de la matriz
print(matrix[1][1])  # Salida: 5

# Definimos una matriz tridimensional (lista de listas de listas)
matrix_0 = [[[1, 2], [3, 4]],
            [[5, 6], [7, 8]]]

# Imprimimos la matriz tridimensional completa
print(matrix_0)  # Salida: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

# Imprimimos el segundo elemento de la matriz tridimensional (segunda lista de listas)
print(matrix_0[1])  # Salida: [[5, 6], [7, 8]]

# Imprimimos el primer sub-elemento del segundo elemento de la matriz tridimensional
print(matrix_0[1][0])  # Salida: [5, 6]

# Imprimimos el primer elemento del primer sub-elemento del segundo elemento de la matriz tridimensional
print(matrix_0[1][0][0])  # Salida: 5