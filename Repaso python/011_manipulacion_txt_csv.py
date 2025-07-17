#leer un archivo linea por linea
'''with open('Repaso python/011_cuento.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())'''

#leer todas las lineas en una lista
'''with open('Repaso python/011_cuento.txt', 'r') as file:
    lineas = file.readlines()
    print(lineas)'''

#agregar texto al final 
'''with open('Repaso python/011_cuento.txt', 'a') as file:
    file.write("\n\n Modificado por Juan Daniel")'''

#sobre escribir archivo
'''with open('Repaso python/011_cuento copy.txt', 'w') as file:
    file.write("\n\n Modificado por Juan Daniel")'''