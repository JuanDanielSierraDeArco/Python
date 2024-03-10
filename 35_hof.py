print('*********Higher order fuction ')

def increment(x):
  return x + 3

def high_ord_func(x, func):

  return x + func(x)

# 2 + (2 + 3)
result = high_ord_func(2, increment)
print(result)


print("*********")

increment_v2 = lambda x : x + 3

high_ord_func_v2 = lambda x, fun : x + fun(x)

print(high_ord_func_v2(2, increment_v2))

print(high_ord_func_v2(2, lambda x : x * 3))
print(high_ord_func_v2(2, lambda x : x - 3))