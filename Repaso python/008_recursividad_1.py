#factorial de un numero

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

valor = int(input("Ingresa un numero => "))
factorial_1 = list(factorial(valor))