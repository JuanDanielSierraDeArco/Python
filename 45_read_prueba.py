import csv

def read_csv(path):
   with open(path, 'r') as csvfile:      
      total = sum(int(r[1]) for r in csv.reader(csvfile))
      return total

response = read_csv('./data.csv')
print(response)