import csv

new_product = {
    'name': 'Cargador celular',
    'price': 15,
    'quantity': 100,
    'brand': 'Jelectric',
    'category': 'Accessories',
    'entry_date': '2025-07-17'
}

with open('Repaso python/products_updated copy.csv', mode='a', newline='') as file:
    #file.write('\n')
    csv_write = csv.DictWriter(file, fieldnames = new_product.keys())
    csv_write.writerow(new_product)