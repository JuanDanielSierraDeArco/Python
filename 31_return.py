sum = 0
for x in range(1, 10):
 sum += x
print(sum)

print("Como una funcion")


def adicion(min, max):
  print(min, max)
  con = 0
  for i in range(min, max):
     con += i
  return(con)

result = adicion(1, 1000)
print(result)