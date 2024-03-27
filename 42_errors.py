#from re import error

print('--------------Manejo de excepciones------------')

try:
  print(0 / 0)
  x = 15
  if x < 18 :
    raise Exception('En esta pagina no se aceptan menores')


except ZeroDivisionError as error:
 print(error)
except Exception as error:
  print(error)


print('proceso.....50%')


try:
  print(0 / 0)
  assert 1 != 1, 'Uno no es igual que uno'
  age = 10
  if age < 18:
    raise Exception('No se permiten menores de edad')
except ZeroDivisionError as error:
  print(error)
except AssertionError as error:
  print(error)
except Exception as error:
  print(error)

print('Hola')
print('Hola 2')