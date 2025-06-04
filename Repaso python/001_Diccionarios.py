
numbers = { 1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
print(numbers)
# Acceso a un elemento
print("Acesso al elemento 2 =>", numbers[2])

information = {
    "name": "Juan Daniel",
    "last_name": "Sierra De Arco",
    "tall": 1.75,
    "age" : 27}
print(information)
del information['age']
print("Informacion sin edad =>", information)
# Agregar un elemento

claves = information.keys()
print("Claves del diccionario =>", claves)
values = information.values()
print("Valores del diccionario =>", values)
pairs = information.items()
print("Pares del diccionario =>", pairs)

contactos = {"Juan Daniel": {"apellido": "Sierra De Arco", "telefono": "123456789", "edad": 27}, 
             "Maria": {"apellido": "Perez", "telefono": "987654321", "edad": 30}}

print("Contactos =>", contactos["Maria"])
print("Contactos =>", contactos.items())
# Agregar un elemento