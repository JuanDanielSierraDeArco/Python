import csv

#leer un archivo
'''with open('Repaso python/products_updated.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)'''

#Mostrar informacion por columnas
'''with open('Repaso python/products_updated.csv') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto : {row['name']}  Precio :{row['price']}")'''
