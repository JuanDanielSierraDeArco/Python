print('******************Map con diccionarios********************')

items = [
  {'producto' : 'camisas', 'price' : 200},
  {'producto' : 'pantalon','price' : 400},
  {'producto' : 'sombrero','price' : 25}
]
print(items)

precios = list(map(lambda items: items['price'], items))
print(precios)

print('**************************************')


def add_taxes(items):
  elment = items.copy()
  elment['taxes'] = elment['price'] * 0.19
  return elment

new_list = list(map(add_taxes, items))
print(new_list)
print(items)

numbers = [1, 2, 3, 4, 5]
def square(x):
    return x ** 2

squares = list(map(lambda y: y + 2, numbers))
print(squares)  # Output: [1, 4, 9, 16, 25]
