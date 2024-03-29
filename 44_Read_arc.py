'''
text = open('./text.txt')



#print(text.read()""


print("leer linea a linea")

print(text.readline())
print(text.readline())
print(text.readline())
print(text.readline())
print(text.readline())

for linea in text:
    print(linea)
text.close()
'''

with open("./text.txt") as text:
    for linea in text:
        print(linea)