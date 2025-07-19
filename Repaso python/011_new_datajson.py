import json

file_path = 'Repaso python/products.json' 

new_producto ={
        "name": "Cargador Juan",
        "price": 200,
        "quantity": 8,
        "brand": "Jelectric",
        "category": "Accessories",
        "entry_date": "2024-01-05"
        }

with open(file_path, 'r') as file:
    Products = json.load(file)

Products.append(new_producto)

with open(file_path, 'w') as file:
    json.dump(Products ,file, indent=4)

