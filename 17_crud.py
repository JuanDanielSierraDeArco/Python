from typing import NewType


print("\n CRUD => Create, Read, Update & Delete\n")

#create
numers = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
print("numeros => ", numers)
#Read
print("\nRead  =>   ", numers[::2])
#Update
numers.append(100)
print(numers)

numers.insert(0, 'Hello')
print(numers)

tasks = ['todo 1', 'todo 2', 'todo 3']
print(tasks)

new_list = numers + tasks
print(new_list)

print(new_list.index('todo 2'))
post = new_list.index('todo 2')

new_list[post] = 'todo change'
print(new_list)
#Delete
new_list.remove('Hello')
print(new_list)
new_list.pop()
print(new_list)
new_list.pop(-2)
print(new_list)
new_list.reverse()
print(new_list)
print()
numers_1 =  [2, 4, 4, 8, 9, 100, 1]
print(numers_1)
numers_1.sort()
print()
print(numers_1)
print()

string = ['ad', 'dr', 'ax', 'aa', 'AA']
print(string)
string.sort()
print(string)
