print('Funcion de recursividad')


def lista_factorial(n):
    if n < 0:
        return []
    else:  
     factoriales = [1] 
     for i in range(1, n + 1):
        factoriales.append(factoriales[-1] * i)
     return factoriales

# Ejemplo de uso
print(lista_factorial(2))  # [1, 1, 2, 6, 24, 120]


print('stado de fibonacci')

def fibonacci_recursivo(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = fibonacci_recursivo(n - 1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

# Ejemplo de uso
print(fibonacci_recursivo(6))  # [0, 1, 1, 2, 3, 5]


def suma_natural(n):
    if n == 0:
        return 0 
    else:
        return n + suma_natural(n -1) 


print(suma_natural(5))


def es_palindromo(cadena):
    cadena = cadena.lower()
    if len(cadena) <= 1:
        return True
    if cadena[0] != cadena[-1]:
        return False
    return es_palindromo(cadena[1:-1])

# Ejemplo de uso
print(es_palindromo("osos"))  # True


