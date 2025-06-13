#manejo de excepciones y erroes

try:
    divisor = int(input("Ingrese un numero =>  "))
    operacion = 100/divisor
    print("El resultado es :", operacion)
except ZeroDivisionError as e:
    print("Error: El divisor no puede ser cero")
    print(e)
except ValueError as e:
    print("Error: debes ingresar un numero")
    print(e)