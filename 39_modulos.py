print('*************** Modulos **************')
import sys

print(sys.path)

print('**************************************')

import re

tex = 'mi numero de telefon es 312 3445 12 34 56 y minumero de la suerte es el 262'

result = re.findall('[0-9]+',tex)
print(tex)
print(result)
print('**************************************')
import time

timestamp = time.time()
print(timestamp)

local = time.localtime()
result_v2 = time.asctime(local)
print(result_v2)

print('**************************************')

import collections

numeros = [1, 3, 2, 5, 2, 5, 6, 7, 2, 2, 1 , 4, 5, 5, 3, 6, 9]
counter = collections.Counter(numeros)
print(counter)