print('******************map********************')


number = [2, 4, 6, 8, 10]
number_v2 = []

for i in number:
  number_v2.append(i * 2)


number_v3 = map( lambda i: i * 2, number_v2)

print(number)
print('**************************************')
print(number_v2)
print('**************************************')
print(list(number_v3))
print('**************************************')