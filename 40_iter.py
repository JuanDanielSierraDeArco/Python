print('------------------Iterators-------------')

print('*********' * 5)
for i in range(1, 6):
  print(i)

print('*********' * 5)
my_iter = iter(range(1, 10))
print(my_iter)
print('*********' * 5)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print('*********' * 5)

my_Pais = ("colombia", "venezuela", "ecuador")
my_pieses = iter(my_Pais)
print(next(my_pieses))
print(next(my_pieses))
print(next(my_pieses))
print('*********' * 5)

print('https://github.com/JuanDanielSierraDeArco')
print('*********' * 5)