def fiboncaci(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fiboncaci(n-1) + fiboncaci(n-2)
    
numero =int(input("Ingrese un numero =>  "))
valor = fiboncaci(numero)
print(valor)