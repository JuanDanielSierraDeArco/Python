# Asignación de una cadena de texto con espacios en blanco al principio y al final
nombre = "   JUAN Daniel"
# Imprime la cadena completa
print(nombre)
# Imprime el primer carácter de la cadena
print(nombre[0])
# Imprime el segundo carácter de la cadena
print(nombre[1])
# Imprime el tercer carácter de la cadena
print(nombre[2])
# Imprime el cuarto carácter de la cadena
print(nombre[3])
# Imprime el último carácter de la cadena
print(nombre[-1])
# Imprime el tipo de dato de la variable 'nombre'
print(type(nombre))

print()  # Imprime una línea en blanco

# Asignación de una cadena de texto sin espacios en blanco al principio y al final
last_name = "sierra de arco"

# Concatenación de las dos cadenas y se imprime
print(nombre + " " + last_name)
# Imprime la longitud total de la cadena resultante de la concatenación
print(len(last_name + ' ' + nombre))

# Imprime la cadena 'nombre' con la primera letra en mayúscula
print(nombre.capitalize())
# Imprime la cadena 'nombre' en mayúsculas
print(nombre.upper())
# Imprime la cadena 'nombre' sin los espacios en blanco al principio y al final
print(nombre.strip())

print('Tipos de datos')

# Asignación de un número entero a la variable 'x'
x = 10
# Asignación de un número de punto flotante a la variable 'y'
y = 5.678
# Asignación de un número en notación científica a la variable 'z'
#z = 1.2e6
# Asignación de otro número en notación científica a la variable 'a'
#a = 2.2e-6

# Imprime el valor de la variable 'x'
print(x)
# Imprime el tipo de dato de la variable 'x'
print(type(x)) 
# Imprime el valor de la variable 'y'
print(y)
# Imprime el tipo de dato de la variable 'y'
print(type(y))
# Imprime el valor de la variable 'z'
#print(z)
# Imprime el tipo de dato de la variable 'z'
#print(type(z))
# Imprime el valor de la variable 'a'
#print(a)
# Imprime el tipo de dato de la variable 'a'
#print(type(a))

# Suma de 'x' consigo mismo e imprime el resultado
print(x + x)
# Suma de 'x' con 'y' e imprime el resultado
print(x + y)
# Suma de 'y' consigo mismo e imprime el resultado
print(y + y)

print('boolean')

# Asignación de valores booleanos a las variables 'is_true' e 'is_false'
is_true = True
is_false = False

# Imprime el valor de 'is_false'
print(is_false)
# Imprime el valor de 'is_true'
print(is_true)
# Imprime el tipo de dato de la variable 'is_false'
print('tipo de dato de is_false', type(is_false))

# Asignación de cadenas de texto a las variables 'frase' y 'autor'
frase = 'nunca pares de aprender'
autor = 'Platzi'

# Imprime la frase y el autor usando coma para la separación
print('Frase:', frase, 'Autor:', autor)

print('Uso del formato f-strings')
# Imprime la frase y el autor usando f-strings
print(f"Frase: {frase}, autor: {autor}")

print('Uso del formato format')
# Imprime la frase y el autor usando el método format
print('Frase: {}, autor: {}'.format(frase, autor))

print('Impresión con formato específico')
# Imprime el valor de 'y' con dos decimales
print('valor y: {:.2f}'.format(y))

print('salto de linea')
# Imprime una cadena con un salto de línea
print('Hola\nmundo')

print("imprimir una cadena con comillas")
# Imprime una cadena que contiene comillas simples
print('Hola soy \'juan\'')

print('imprimir una ruta de un archivo')
# Imprime una cadena que representa una ruta de archivo con doble barra invertida
print('La ruta del archivo es: c:\\Users\\Usuario\\Desktop\\archivo.txt')
