import random

print("        🕹️  JUGUEMOS 🕹️\n")

options = ('piedra', 'papel', 'tijera')


computer_wins = 0
user_wins = 0
rounds = 1

while True:
  print("*" * 30)
  print("*   🧙‍♂️   ROUND => {}   🤖    *".format(rounds))
  print("* Usuario {}   Computadora {}  *".format(user_wins, computer_wins))
  print("*" * 30)

  user_option = input("\npiedra🪨   papel📰   tijera✂️   =>")
  user_option = user_option.lower()
  
  if not user_option in options:
    print("Esa opcion no es valida")
    continue
  
  computer_option = random.choice(options)
  print()
  print("User Option =>", user_option)
  print("Computer potion =>", computer_option)
  print()
  
  if (user_option == computer_option):
    print("empate!\n")
  elif (user_option == 'piedra'):
       if (computer_option == 'tijera'):
         print("piedra gana a tijera")
         print("usuario gano!\n")
         user_wins +=1
       else:
         print("papel gana a piedra")
         print("gana la computadora\n")
         computer_wins +=1
  elif (user_option == 'papel'):
      if (computer_option == 'piedra'):
        print("papel gana a piedra")
        print("gana el usuario\n")
        user_wins +=1
      else:
        print("tijera gana papel")
        print("gana la computadora\n")
        computer_wins +=1
  elif (user_option == 'tijera'):
        if (computer_option == 'papel'):
          print("tijera gana a papel")
          print("gana el usuario\n")
          user_wins +=1
        else:
          print("piedra gana tijera")
          print("gana la computadora\n")
          computer_wins +=1
  if computer_wins == 3:
    print("*" * 31)
    print("*         COMPUTADORA         *")
    print("*" * 31)
    print("*      *   *  ***  *   *   ** *")
    print("*     *   *   *   *   *  *  * *")
    print("*    *   *   *   * * *   *    *")
    print("*   * * *   *   *  **    *    *")
    print("*  * * *   *   *   *  *  *    *")
    print("*  * *   ***  *   *   **      *")
    print("*" * 31)
    break
  elif user_wins == 3:
    print("*" * 31)
    print("*            USUARIO          *")
    print("*" * 31)
    print("*      *   *  ***  *   *   ** *")
    print("*     *   *   *   *   *  *  * *")
    print("*    *   *   *   * * *   *    *")
    print("*   * * *   *   *  **    *    *")
    print("*  * * *   *   *   *  *  *    *")
    print("*  * *   ***  *   *   **      *")
    print("*" * 31)
    break
  rounds += 1