from collections import Counter


print("-----------loops  while----------\n")

counter = 0
counter_1 = 0
counter_2 = 0

''''
while True:
  print("Se ejecuto")
'''

while counter < 10:
  print(counter)
  counter += 1
  
print()

while counter_1 < 20:
  print(counter_1)
  counter_1 += 1
  if counter_1 == 15:
     print("STOP")
     break
  
print()

while counter_2 < 20:
  counter_2 += 1
  if counter_2 < 15:
     continue
    
  print(counter_2)