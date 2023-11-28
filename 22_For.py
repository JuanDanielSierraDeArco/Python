print("------------Ciclo for-----------\n")
'''
for element in range(1, 20):
  print(element)
'''

'''
for element in range(1,2,2):
  print(my_list[element])
'''

my_list = ['rojo', 'verde', 'azul', 1, 2, 3, 'casa']
for i in my_list:
 print(i)

my_tuple = ('Enero', 'Febrero', 'Marzo',)
for i in my_tuple:
  print(i)

person = {
  'color' : 'blanco, negro',
   'ojos' : 'cafes',
   'tall' : '1.75',
   'age' : 25
}
print()
for i in person:
  print(i, "=>", person[i])

for key, value in person.items():
 print(key, "=>",value)

people =[
  {'name' : 'juan',
   'last_name' : 'Sierra'
  },
  { 'name' : 'Daniel',
    'last_name' : 'Sierra'
  }
]
for person in people:
  print(person)
print()

for person in people:
  print("name =>", person['name'], "", person['last_name'])