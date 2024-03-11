def filter_by_length(words):
  palabra = list(filter(lambda x : len(x) >= 4, words))
  return palabra

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)