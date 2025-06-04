#Generador

def generador():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

for value in generador():
    print(value)