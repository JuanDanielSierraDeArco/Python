print("o, 1, 1, 2 , 3, 5, 8, 13 ....")


def fibonacci(limite):
    a, b = 0, 1
    while a < limite:
        yield a
        a, b = b, b + a

for num in fibonacci(10):
 print(num)



 def numeros(limite):
    z = 1
    while z <= limite:
     if (z % 2) == 0:
       yield z
     z += 1
       
       
for x in numeros(10):
   print(x)
   