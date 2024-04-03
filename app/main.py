import element
import read_csv
import charts

def run():
  data = read_csv.read_csv('./app/Data_pop.csv')
  contin_list = list(set(map( lambda x: x['Continent'],data)))
  print('!Puedes elegir un continente!\n')
  for a in contin_list:
   print('=>',a)
  save_cont = input('\n=>')
  save_cont = save_cont.title()
  data = list(filter(lambda item: item['Continent'] == save_cont, data))
  country = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'],data))

  country_list = list(set(country.copy()))
  charts.generate_tort_char(country, percentages)

  print(f'!Puedes elegir un Pais del {save_cont}!')
  for a in country_list:
   print('=> ',a)

  country_1 = input('\n=>') 
  country_1 = country_1.title()
  result = element.population_by_country(data, country_1)

  if len(result) > 0:
    country = result[0]
    labels, values = element.get_population(country)
    charts.generate_bar_char(labels, values)

if __name__ == '__main__':
  run()
