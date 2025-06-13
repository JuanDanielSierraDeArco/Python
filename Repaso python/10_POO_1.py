#programacion orientada a objetos

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hola mi nombre es {self.name} y tengo {self.age} años un gusto en conocerte")

Persona1 = Person("ana",25)
Persona2 = Person("Juan",27)

Persona1.greet()
Persona2.greet()