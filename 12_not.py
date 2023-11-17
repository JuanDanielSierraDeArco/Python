print("----------Operador Logico not------\n")

print("no True => ", not True)
print("not False => ", not False)

print("----------Operador not and-------------")

print(" not (True and True) =>", not (True and True))
print(" not(True and False) =>", not (True and False))
print("not (False and True) =>", not (False and True))
print("not (False and False) =>", not(False and False))

stock = int(input("ingrese el numero de stock =>"))

print(not (stock >= 100 and stock <= 1000))