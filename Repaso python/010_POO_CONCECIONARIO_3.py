class Car:
    def __init__(self,brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.available = True

    def sell(self):
        if self.available:
            self.available = False
            print(f"El coche {self.brand} {self.model} ha sido vendido")
        else:
            print(f"El coche {self.brand} {self.model} no esta dispoible")
    def check_availability(self):
        return self.available
    
    def get_price(self):
        return self.price
class Customer:
    def __init__(self, name):
        self.name = name
        self.cars_purchased = []
    
    def buy_car(self, car):
        if car.check_availability():
            car.sell()
            self.cars_purchased.append(car)
        else:
            print(f"Lo siento, {car.brand} {car.model} no esta disponible.")
    
    def inquire_car(self, car):
        availability = "disponible" if car.check_availability() else "no dispobible"
        print(f"El coche {car.brand} {car.model} es {availability} y cuesta {car.price}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_car(self, car):
        self.inventory.append(car)
        print(f"El coche {car.brand} {car.model} ha sido añadido al inventario.")

    def register_customer(self, customer):
        print(f"El cliente {customer.name} ha sido registrado en la concesionaria.")

    def show_available_cars(self):
        print("Coches disponibles en la concesionaria:")
        for car in self.inventory:
            if car.check_availability():
                print(f"- {car.brand} {car.model} por {car.get_price()}") 


# Crear coches
coche1 = Car("Toyota", "Corolla", 18000)
coche2 = Car("Honda", "Civic", 20000)
coche3 = Car("Ford", "Mustang", 35000)

# Crear concesionaria
mi_concesionaria = Dealership()

# Añadir coches al inventario
mi_concesionaria.add_car(coche1)
mi_concesionaria.add_car(coche2)
mi_concesionaria.add_car(coche3)

# Mostrar coches disponibles
mi_concesionaria.show_available_cars()

# Crear un cliente
cliente1 = Customer("Ana")

# Registrar cliente
mi_concesionaria.register_customer(cliente1)

# Cliente consulta coche
cliente1.inquire_car(coche1)

# Cliente compra coche
cliente1.buy_car(coche1)

# Cliente intenta comprarlo de nuevo
cliente1.buy_car(coche1)

# Mostrar coches disponibles después de la compra
mi_concesionaria.show_available_cars()
