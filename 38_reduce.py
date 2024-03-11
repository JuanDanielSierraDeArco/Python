import functools

print('*************** Reduce **************')

numbers = [1, 2, 3, 4]

def accum(counter, item):
  print('Counter =>',counter)
  print('Item =>',item)

  return counter + item

result_v2 = functools.reduce(accum, numbers)
print(result_v2)

print()
result = functools.reduce(lambda counter, item : counter + item, numbers)
print(result)

print('***************************************')