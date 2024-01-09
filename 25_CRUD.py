print("Modificando conjuntos")

set_countries = {'colombia', 'mexico', 'venezuela', 'peru', 'brazil', 'portugal'}
print("Conjunto de paises",set_countries)

size = len(set_countries)
print("Cantidad de paises",size)
print()

print("Quiero saber si colombia esta en el comjunto de paises?")
if 'colombia' in set_countries:
  print("SI")

  
# Add
print()
print("Quiero agregar elementos a mi conjunto")
print(set_countries)
set_countries.add('ecuador')
print(set_countries)
print()

# Update
print("Quiero actulizar mi conjunto")
set_countries.update({'argentina', 'bolivia'})
print(set_countries)
print()
# Remove, puedes utilizar discard para que no lance errror 
print("Como puedo eliminar elemento de mis cojuntos")
set_countries.remove('portugal')
print(set_countries)
set_countries.clear()
print(set_countries)