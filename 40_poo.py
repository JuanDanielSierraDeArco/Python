class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f'Hola mi nombre es {self.name} y tengo {self.age} años de edad y este poo')



person1 = Person('juan daniel', 25)
person2 = Person('daniel juan', 36)

person1.greet()
person2.greet()