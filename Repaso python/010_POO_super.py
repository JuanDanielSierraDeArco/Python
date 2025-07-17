
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def great(self):
        print(f"Hola soy una persona me llamo {self.name} y tengo {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def great(self):
        print(f"Hola un estudiante y  me llamo {self.name} y tengo {self.age} con el codigo {self.student_id}")

alguien = Student("Juan Daniel", 27, "T29")
alguien.great()