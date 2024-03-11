import utils

keys, values = utils.get_population()
print(keys, values)

pais = [
  {'Country' : 'colombia', 'Population' : 800},
  {'Country' : 'peru', 'population' : 500},
  {'Country' : 'brazil', 'population' : 1000},
  {'Country' : 'venezuela', 'population' : 900},
  {'Country' : 'mexico', 'population' : 1200}
]

print(pais)
print()
po_pais = utils.population_by_country(pais, 'colombia')
print(po_pais)