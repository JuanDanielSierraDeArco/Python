from eleme import element

pais = [
  {'Country' : 'colombia', 'Population' : 800},
  {'Country' : 'peru', 'population' : 500},
  {'Country' : 'brazil', 'population' : 1000},
  {'Country' : 'venezuela', 'population' : 900},
  {'Country' : 'mexico', 'population' : 1200}
]

def run():
  keys, values = element.get_population()
  print(keys, values)
  print(pais)
  print()
  Country = input('Pais =>')
  po_pais = element.population_by_country(pais, Country)
  print(po_pais)

if __name__ == '__main__':
  run()
