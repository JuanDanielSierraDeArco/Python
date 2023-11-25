print("------------------Float-----------------\n")

x = 3.3
print("El valor de X => ", x)
print()

z = 1.1 + 2.2
print()

print("Tengo una variable z = 1.1 + 2.2 =>  ")
print("El valor de z => ", z)
print("vamos a compara dos numeros flotantes modo string")

print("para compararlos agregamos el formato a string")
z_string = format(z, '.2g')
print(z_string)
print()
print(z_string == str(x))
print("-"*20)

tolerancia = 0.00001


print(abs(z - x) < tolerancia)
