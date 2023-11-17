print(".............................STRING...............")
# esto es una cadena de texto.
my_name = "Juan"
last_name = "Sierra De Arco"
edad = "25"
print()
print(my_name)
print(last_name)
print(edad)
print()
full_name = my_name + " " + last_name + " " + edad
print(full_name)
quote = "I'm a Juan."
print(quote)
print()

# format.

teample = "My nombre es " + my_name + " y mi apellido es " + last_name + " y Tengo " + edad + " años";
print('v1', teample)

teample = "My nombre es {} y mi apellido es {} y tengo {} años".format(my_name, last_name, edad)
print('v2', teample)

teamplate = f"my nombre es {my_name} y mi aplellido {last_name}"
print('v2', teamplate)
