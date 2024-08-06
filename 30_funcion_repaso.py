# calculadora
def add(num1, num2):

    return num1 + num2

def sustraction(num1, num2):

    return num1 - num2


def multiplication(num1, num2):

    return num1 * num2

def divition(num1, num2):

    return num1 / num2

def calculadora():
    print('Bienvenido a las operaciones')
    while True:
        print('Elige la operacion que deseas realizar')
        print('1. para sumar')
        print('2. para restar')
        print('3. para multiplicar')
        print('4. para dividor')
        print('5. para salir')
        operation = input('==>')

        if operation == "5":
            print('saliendo de la calculadora')
            break
        
        if operation in [ '1', '2', '3', '4']:
            num1 = float(input('ingresa primer numero =>'))
            num2 = float(input('ingresa primer numero =>'))

            if operation == '1':
                print('El resultado es =>', add(num1,num2))

            elif operation == '2':
                print('El resultado es =>', sustraction(num1,num2))
            
            elif operation == '3':
                print('El resultado es =>', multiplication(num1,num2))
            
            elif operation == '4':
                print('El resultado es =>', divition(num1,num2))
        
        else:
          print('Operacion invalida')


calculadora()