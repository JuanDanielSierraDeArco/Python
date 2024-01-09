print("-------------Diccionarios--------\n")

my_dict = {
  'avion': 'bla bla bla',
  'name': 'juan',
  'last_name': 'Sierra De Arco',
  'age': 25
}
print(type(my_dict))
print(my_dict)
print(len(my_dict))
print()

print(my_dict['age'])
print(my_dict.get('age'))
print('avion' in my_dict)
print('avi' in my_dict)