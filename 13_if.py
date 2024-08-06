print("--------Condicional if --------")

# Ejemplo básico de condicional if
if True:
    print("debería ejecutarse")

if False:
    print("Nunca se ejecuta")

# Solicita al usuario que ingrese su mascota favorita y guarda la entrada en la variable 'pet'
pet = input("¿Cuál es tu mascota favorita? ")

# Condicionales para evaluar la mascota favorita del usuario
if pet == 'perro':
    print("Tienes buen gusto")
elif pet == 'gato':
    print("Genial, ¡que tengas buena suerte!")
elif pet == 'pez':
    print("Eres lo máximo")
else:
    print("No tienes ninguna mascota interesante")

# Comentario del bloque que sigue
'''
stock = input("Digital el stock => ")
stock = int(stock)

# Condicional para verificar si el stock está en el rango correcto
if stock >= 100 and stock <= 1000:
    print("El stock es correcto")
else:
    print("El stock es incorrecto")
'''
# Programa para calcular si un número es par o impar
print("Programa para calcular si un número es par o impar")

# Solicita al usuario que ingrese un número y guarda la entrada en la variable 'valor'
valor = int(input("Ingrese el número que desea verificar: "))

# Condicional para verificar si el número es par o impar
if valor % 2 == 0:
    print("El número {} es par".format(valor))
else:
    print(f"El número {valor} es impar")
