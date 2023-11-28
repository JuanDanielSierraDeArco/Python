print("STRING");
# esto es una cadena de texto.
my_name = "Juan";
last_name = "Sierra De Arco";

print(my_name);
print(last_name);

full_name = my_name + " " + last_name;
print("My full name is", full_name);

quote = "I'm a Juan.";
print(quote);

# format.

teample = "My nombre es " + my_name + " y mi apellido es " + last_name;
print('v1', teample);

teample = "My nombre es {} y mi apellido es {}".format(my_name, last_name);
print('v2', teample);

teamplate = f"my nombre es {my_name} y mi aplellido {last_name}";
print('v2', teamplate);