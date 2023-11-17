import random

options = ('piedra', 'papel', 'tijera')
user_option = input("piedra, papel o tijera =>")
user_option = user_option.lower()

if not user_option in options:
  print("Esa opcion no es valida")

computer_option = random.choice(options)

print("\nUser Option =>", user_option)
print("Computer potion =>", computer_option)
print()

if (user_option == computer_option):
  print("empate!")
elif (user_option == 'piedra'):
     if (computer_option == 'tijera'):
       print("piedra gana a tijera")
       print("usuario gano!")
     else:
       print("papel gana a piedra")
       print("gana la computadora")
elif (user_option == 'papel'):
    if (computer_option == 'piedra'):
      print("papel gana a piedra")
      print("gana el usuario")
    else:
      print("tijera gana papel")
      print("gana la computadora")
elif (user_option == 'tijera'):
      if (computer_option == 'papel'):
        print("tijera gana a papel")
        print("gana el usuario")
      else:
        print("piedra gana tijera")
        print("gana la computadora")