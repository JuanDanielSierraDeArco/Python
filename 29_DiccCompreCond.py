print(" Diccionary Comprehesion Condition")

import random

Contries = [ 'col', 'mex', 'bol', 'per', 'ven']
population = {country : random.randint(100, 5000) for country in Contries}
print(population)

print()
print("Paise con poblacion superior de 1000")
result = {country : population for (country, population) in population.items() if (population > 2000)}
print(result)

print()
tex = 'Hola, soy juan y estos son mis temas de estudio'

unique = { i : i.upper() for i in tex if i in 'aeiou'}
print(unique)