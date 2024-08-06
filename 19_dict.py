print("-------------Diccionarios--------\n")

numbers = {1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco"}

print(numbers)
print(numbers[4])
print(numbers.keys())
print(numbers.values())

information = { "Nombre" : "Juan Daniel",
               "Apellido": "Sierra De Arco",
               "Altura" : 1.73,
               "Edad" : 25}
print(information)
claves = information.keys()
print(claves)

values = information.values()
print(values)

pares = information.items()
print(pares)

contactos = {"Juan" : {
               "Apellido": "Sierra De Arco",
               "Altura" : 1.73,
               "Edad" : 25}, 
               "Daniel" : {
               "Apellido": "Sierra De Arco",
               "Altura" : 1.73,
               "Edad" : 28},
               "pedro" : {
               "Apellido": "Sierra De Arco",
               "Altura" : 1.73,
               "Edad" : 30}}

print(contactos.keys())
print(contactos.values())
