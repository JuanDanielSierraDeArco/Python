
def fibonacci(n):
    if n == 0:
        return [0]
    elif n == 1:

        return [0 ,1]
    else:
        list_fibonacci = fibonacci(n - 1)
        list_fibonacci.append(list_fibonacci[n - 1] + list_fibonacci[n - 2])
        return list_fibonacci
    
print(fibonacci(15))

def suma_natural(n):
    if n == 0:
        return [0] 
    else:
        list_natural = suma_natural(n - 1)
        list_natural.append(n + list_natural[n -1]) 
        return  list_natural

print(suma_natural(15))