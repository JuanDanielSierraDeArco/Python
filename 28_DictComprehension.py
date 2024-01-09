print(" Dictionaty Comprehesion")

person = {
  'name' : 'juan',
  'last_name' : 'sierra de Arco',
  'Age' : 25
}

numers = {}
for i in range(1,5):
  numers[i] = i * 2
print(numers)

numers_v2 = { i : i * 2 for i in range(1, 5) }
print(numers_v2)

Contries = [ 'col', 'mex', 'bol', 'per', 'ven']
population = {}

print()
import random
for pais in Contries:
  population[pais] = random.randint(1, 1000)

print(population)

print()
population_v2 = { country: random.randint(100, 1000) for country in Contries}
print(population_v2)

print()
names = ['juan', 'daniel', 'sierra']
ages = [12, 24, 36]


print(dict(zip(names, ages)))

print()
new_dic = {names : ages for (names, ages) in zip (names, ages)}
print(new_dic)