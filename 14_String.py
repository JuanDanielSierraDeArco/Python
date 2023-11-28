print("______________STRING____________\n")

text = 'Ella sabe programar en python'
print(text)
print()

print("En el texto esta la palabra javaScript => ",'javaScript' in text)
print("En el texto esta la palabra python => ",'python' in text)
# in, buscar carateres en un string
if 'python' in text:
  print("Elegiste bien python!")
else:
  print("Tambien elegistes bien")
#calcular el tamaño de un string
size = len(text)
print("El tamaño del string es =>", size)
#text.upper() me convierte todo el texta a mayuculas
#text.lower() me conviente todo el texto a minuculas 
print(text)
print(text.lower())
print(text.upper())
print("cuantas veces esta la letra 'a' => ", text.count('a'))
print(text.swapcase())
print(text.startswith('Ella'))
print(text.endswith('Rush'))
print(text.endswith('python'))
print(text.replace('python', 'Go'))

text_2 = 'este es un titulo'
print(text_2)
print(text_2.capitalize())
print(text_2.title())