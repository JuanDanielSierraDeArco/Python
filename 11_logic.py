print("\n----------Operadores Logicos-----------\n")

print("----------Operador and-------------")

print("True and True =>", True and True)
print("True and False =>", True and False)
print("False and True =>", False and True)
print("False and False =>", False and False)
print("----------ejemplos------")
print("10 > 5 and 5 < 10 ==>", 10 > 5 and 5 < 10)
print("10 > 5 and 5 > 10 ==>", 10 > 5 and 5 > 10)

stock = input("Ingrese el numero de stock =>")
stock =  int(stock)
print("Estado STOCK =>", stock > 100 and stock <= 1000)

print("----------Operador OR-------------")

print("True or True =>", True or True)
print("True or False =>", True or False)
print("False or True =>", False or True)
print("False or False =>", False or False)
print("----------ejemplos------")
role = input("Digite el rol => ")
print(role == 'admin' or role == 'seller')