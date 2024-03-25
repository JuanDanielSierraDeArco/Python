'''
from compras import orders
'''

def get_totals(x):
   Dato = x.copy()
   return [order['total'] for order in Dato]
  
def calc_total(totals):
   return sum(totals)



'''
prueba_1= get_totals(orders)
prueba_2 = calc_total(prueba_1)
print(prueba_1)
print(prueba_2)

'''
