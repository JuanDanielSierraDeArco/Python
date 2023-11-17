print("--------Condicional if --------")

if True:
  print("deberia ejecutarse")

if False:
  print("Nunca se ejecuta")


pet = input("Cuanl es tu mascota favorita ? ")

if pet == 'perro':
  print("Tienes buen gusto")

elif pet == 'gato':
  print("genial que tengas buena suerte")

elif pet == 'pez':
  print("eres lo maximo")

else:
  print("No tienes ninguna mascota interesante")

'''
stock = input("Digital el stock => ")
stock = int(stock)

if stock >= 100 and stock <= 1000 :
  print("El stock es correcto")
else:
  print("El es stock es incorrecto")
'''

print("Progrmam para calcular si un numero es par")

valor = int(input("Ingrese el numero que desea comprobar =>"))

if (valor % 2 == 0):
  print("El numero {} es par".format(valor))
else:
  print(f"el numero {valor} es impar")