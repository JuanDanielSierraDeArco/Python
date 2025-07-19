import csv

file_path = 'Repaso python/products.csv'
updated_file_path = 'Repaso python/products_modific.csv'

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    #obtener los nombre de las colimnas existentes
    fieldnames = csv_reader.fieldnames + ['total_values']
     
    with open(updated_file_path, mode='w', newline='') as update_file:
        csv_writer = csv.DictWriter(update_file, fieldnames = fieldnames)
        csv_writer.writeheader() # escribir encabezado

        for row in csv_reader:
            row['total_values'] = float(row['price']) * int(row['quantity'])
            csv_writer.writerow(row)

