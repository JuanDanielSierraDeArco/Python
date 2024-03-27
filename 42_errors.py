#from re import error

print('--------------Manejo de excepciones------------')

try:
  print(0 / 0)
except ZeroDivisionError as error:
 print(error)

print('proceso.....50%')