print('******** FUNCIONES LAMBDAS**********')

def increment(x):
  return x + 1
  
print(increment(100))

increment_v2 = lambda x : x + 1

print(increment_v2(200))

full_name = lambda name, last_name : f'full name es {name.title()} {last_name.title()}'


print(full_name('juan', 'sierra de arco'))
