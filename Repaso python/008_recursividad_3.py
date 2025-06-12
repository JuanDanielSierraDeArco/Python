# numeros naturales

def add_num(n):
    if n==0:
      return 0
    else:
       return n + add_num(n-1)
    
numero = int(input("Ingrese un numero => "))

valor = add_num(numero)
print(valor)