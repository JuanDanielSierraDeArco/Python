x = 3.3
print(x)
print()
y = 1.1 + 2.2
print(y)
print()
print( x == y)

print("vamos a compara dos numeros flotantes modo string\n")

y_string = format(y, '.2g')
print(y_string)
print()
print(y_string == str(x))
print("-"*20)

tolerancia = 0.00001


print(abs(y - x) < tolerancia)
