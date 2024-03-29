with open("./text.txt", 'r+') as text:
    for linea in text:
        print(linea)
        
    print()
    
    text.write('nuevas cosa en este archivo')