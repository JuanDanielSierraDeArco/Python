print("------------Disccionarios---------\n")

person = {
  'name' : 'Juan',
  'last_name' : 'Sierra',
  'lengs' : ['python', 'JavaScript'],
  'age' : 25  
}
print(person)
print()
person['name'] = 'Daniel'
print(person)

person['age'] -= 2
print(person)

del person['last_name']
print(person)
person.pop('age')
print(person)

print("Items")
print(person.items())

print("keys")
print(person.keys())

print("values")
print(person.values())