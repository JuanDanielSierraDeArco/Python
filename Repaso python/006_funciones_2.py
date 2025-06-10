#Calculadora

def add(a,b):
    return a + b

def sustration(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def divide(a,b):
    return a / b

def calculadora():
    while True:
        print("Calculadora elija una opcion")
        print("1. suma")
        print("2. resta")
        print("3. multiplicar")
        print("4. dividir")
        print("5. salir")
        option = input("Ingrese una option => ")

        if option == "5":
            print("saliendo de la calculadora")
            break

        elif option in ["1", "2", "3", "4"]:
            num1 = float(input("ingrese primer numero =>"))
            num2 = float(input("ingrese segundo numero =>"))

            if option == "1":
                print("la suma es =>", add(num1,num2))
            
            elif option == "2":
                print("la resta es =>", sustration(num1,num2))
            
            elif option == "3":
                print("la multiplicacion es =>", multiplicacion(num1,num2))
            
            else:
                print("la division es =>", divide(num1,num2))
        
        else:
            print("operacion no valida")

calculadora()