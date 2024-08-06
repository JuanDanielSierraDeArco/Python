print('******** FUNCIONES LAMBDAS**********')

def increment(x):
  return x + 1
  
print(increment(100))

increment_v2 = lambda x : x + 1

print(increment_v2(200))

full_name = lambda name, last_name : f'full name es {name.title()} {last_name.title()}'


print(full_name('juan', 'sierra de arco'))


base = int(input('ingrese valor de la base =>'))
altura = int(input('Ingrese valor de la altura =>'))
area = lambda base, altura: (base * altura)/2

print(area(base,altura))

number = range(11)
squared_number = list(map(lambda x: x**2, number))
print(squared_number)
event_nummbers = list(filter(lambda x: x%2 == 0, number))
print('numeros pares con lambda\n', event_nummbers)