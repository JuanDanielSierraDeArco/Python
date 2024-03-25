import element

orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]

def get_total(orders):

   totals = element.get_totals(orders)
   Sum = element.calc_total(totals)
   return Sum



total = get_total(orders)
print(total)


