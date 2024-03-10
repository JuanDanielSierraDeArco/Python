
#from typing import Text


def find_volumen(langth = 1, width = 1, depth = 1):
  return langth * width * depth, width, 'hola'

result = find_volumen(10, 20, 3)
print(result)

result = find_volumen(0, 0, 0)
print(result)

result = find_volumen()
print(result)

result = find_volumen(depth= 20)
print(result)

result = find_volumen(depth= 20)
print(result)

result, width, Text = find_volumen(depth= 20)
print(result)
print(width)
print(Text)