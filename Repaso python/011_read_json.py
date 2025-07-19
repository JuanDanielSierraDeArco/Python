import json

#Lectura del archivo
with open('Repaso python/products.json', 'r') as file:
    products = json.load(file)


for product in products:
    print(f"Producto => {product['name']} Precio => {product['price']}")