#List comprehension numeros al cuadrado
#square = [ x**2 for x in range(1,11)]
#print(square)

# coversio de grados celcius a fahrenheit
#celsius = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#farenheit = [(((i)*(9/5)) + 32) for i in celsius]
#print(farenheit)

#numeros pares
evens = [ x for x in range(1,100) if x % 2 == 0] 
#print(evens)
#numeros pares
odd_numbers = [ x for x in range(1,100) if x % 2 != 0] 
#print(odd_numbers)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(matrix)
print(transposed)