print()
print("---------------------Numeros----------------------------------")
print()

lives = 3
print(type(lives))
print()

age = 25
buget = 1000
print(age)
print(buget)

temperatura = 38.1214
print(type(temperatura))

lives = 2
print("perdiste una vida tienes =", lives)

lives = 12 + 12
print("tienes una bonificacion de vidas", lives)

lives = lives - 6
print(lives)

numer = 1600000000000000000000.4
print(numer)
print()

nombre = input("Bienvenido como te llamas ")
print()
print("HI, Bienvenido {} calcularesmos el promedio de tu presupuesto en 5 meses".format(nombre))
print()
print( "Acontinuacion te voy a pedir tus gastos en estos 5 meses. ")
print("!Esta bien {}!".format(nombre))
print()
G_enero = int(input("Ingresa el valor de tus gastos en el mes 1 "))
G_febrero = int(input("Ingresa el valor de tus gastos en el mes 2 "))
G_marzo = int(input("Ingresa el valor de tus gastos en el mes 3 "))
G_abril = int(input("Ingresa el valor de tus gastos en el mes 4 "))
G_mayo = int(input("Ingresa el valor de tus gastos en el mes 5 "))
print()
G_promedio = ((G_enero + G_febrero + G_marzo + G_abril + G_mayo) / 5)
print("Tu promedio de gastos en 5 meses es de ", G_promedio)
