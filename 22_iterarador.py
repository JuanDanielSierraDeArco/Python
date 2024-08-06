# ejemplo de iterador 

#Definicion de una lista de ejemplo
my_list = [1, 2, 3, 4, 5, 6, 7]

#creacion de un iterador apartir de una lista
my_iter = iter(my_list)

#uso de next para obtener cada uno de los elementos de la lista
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


#ejempo de iterador con una cadena de texto en python
#definicion de una cade de texto
cade_text = "HOLA MUNDO"

# creacion de un iterador apartir de una cadena de texto
iter_cadena = iter(cade_text)

#uso del bucle for para iterar sobre cada caracter del del iterador
for caracter in iter_cadena:
    print(caracter)

#crear uniterador para numeros impares
#definimos un limite para los numeros que deseamos mostrar
limite = 10

#creamos un iterador apartir del limite mediante la utilizacion de la funcion range
iter_impar = iter(range(1,limite + 1, 2))

#Uso del bucle for para iterar sobre cada caracter elemento del iterador
for num_impar in iter_impar:
    print(num_impar)

#Uso de generador
#Definicion de una funcion generadora
def generador():
    yield 1
    yield 2
    yield 3

#Uso del bucle for para iterar lo elementos generados
for num in generador():
    print(num)

#practica de fibonacci

def serie(stop_1):
    a, b = 0 , 1
    while (a <= stop_1):
        yield a
        a, b = b, a + b

for num in serie(100):
    print(num)


#numeros pares 

def gene_pares(rango):
    stop_2 = 1
    while stop_2 <= rango:
        if (stop_2 % 2 == 0):
            yield stop_2
            stop_2 += 1
        else:
            stop_2 += 1

for pares in gene_pares(20):
    print('Este numero {} es par '.format(pares))

def gene_impares(rango):
    stop_2 = 1
    while stop_2 <= rango:
        if (stop_2 % 2 != 0):
            yield stop_2
            stop_2 += 1
        else:
            stop_2 += 1

for impares in gene_impares(20):
    print('Este numero {} es impar '.format(impares))