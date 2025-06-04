numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''for i in numbers:
    print("Aqui I es igual => ",i)'''

'''for i in numbers:
    print("Aqui i es igual => ", i + 1)'''

'''for i in range (10):
    print(i)'''

for i in range (3, 10):
    print(i)

fruits = ["manzana", "pera", "naranja", "plátano"]
for i in fruits:
    if i == "naranja":
        print("naranja encontrada en la lista")
    else:
        print(i)
x= 0
while x < 5:
    if x == 3:
        break
    else:
        print(x)
        x += 1

for i in range (15):
    if i == 10 or i == 5 or i == 15:
        continue
    print(i)