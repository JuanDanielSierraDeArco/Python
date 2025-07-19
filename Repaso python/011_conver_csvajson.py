import csv
import json

file_path_csv = 'Repaso python/products.csv'
file_path_json = 'Repaso python/011_nuevo_json.json'

# pasar del archivo csv a json
#abrir el archivo csv

with open(file_path_csv, 'r') as file_csv:
    csv_reader = csv.DictReader(file_csv)

    #convertir filas en una lista de diccionarios
    filas = list(csv_reader)
    print(filas)

with open(file_path_json, 'w') as file_json:
    json.dump(filas, file_json, indent=4)