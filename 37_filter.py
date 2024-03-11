print('*************** filter() **************')

'''FILTER La función filter(), devuelve un valor que esta siendo iterado de la cual su resultado será el valor que se esta buscando en el filter
SINTAXIS filter (function, iterable) '''

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

new_numbers = filter(lambda x : x % 2 == 0, numbers)
print(new_numbers)

new_numbers = list(new_numbers)
print(new_numbers)

print('***************************************\n')

def filter_by_length(words):
  palabra = list(filter(lambda x : len(x) >= 4, words))
  return palabra

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(words)
print(response)

print('***************************************\n')

ages = [5, 12, 17, 18, 24, 32]
print('Edad de personas',ages)

def my_funtion(x):
  if x > 18 :
    return True
  else :
   return False

adults = list(filter(my_funtion, ages))
print('personas mayores')
print(adults)
menores = adults = list(filter(lambda x : not my_funtion(x), ages))
print('personas menores')
print(menores)




print('***************************************\n')