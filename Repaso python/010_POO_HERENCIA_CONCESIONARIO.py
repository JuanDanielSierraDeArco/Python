#ejercicio para enteder los cautro pilares de POO Abstraccion, Encapsulamiento, Herencia y Polimorfismo 
class Vehicle:
    def __init__(self, brand, model, price):
       #Encapsulación 
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El coche {self.brand} {self.model} ha sido vendido")
        else:
            print(f"El coche {self.brand} {self.model} no esta disponible")
    #abstracción
    def check_available(self):
        return self.is_available
    #abstracción
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado en la siguiete clase")
    
    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado en la siguiente clase")
#herencia  
class Car(Vehicle):
    #Polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} esta en marcha"
        else:
            return f"El coche {self.brand} no esta disponible"
    #Polimorfismo
    def stop_engine(self):
        if self.is_available:
            return f"El motor del coche {self.brand} se ha detenido"
        else:
            return f"El coche {self.brand} no esta disponible"

class Bike(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"La Bicicleta {self.brand} esta en marcha"
        else:
            return f"La Bicicleta {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"La Bicicleta {self.brand} se ha detenido"
        else:
            return f"La Bicicleta {self.brand} no esta disponible"

class Truck(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"El motor del Camión {self.brand} esta en marcha"
        else:
            return f"El Camión {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"El motor del Camión {self.brand} se ha detenido"
        else:
            return f"El Camión {self.brand} no esta disponible"

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []
    
    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Lo siento, {vehicle.brand} no esta diponible")
    
    def inquiere_vehicle(self, vehicle:Vehicle):
        if vehicle.check_available():
            availability = "Disponible"
        else:
            availability = "No dispnible"
        
        print(f"El vehiculo {vehicle.brand} {availability} y cuestas {vehicle.get_price()}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []
    
    def add_vehicles(self, vehicle:Vehicle):
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido añadido al invetario")

    def register_customers(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido registrado")

    def show_available_vehicles(self):
        print(f"Vehiculos disponibles en la tienda")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- El {vehicle.brand} por {vehicle.get_price()}")

#vehiculos
car1 = Car("Toyota", "Corrola", 20000)
bike1 = Bike("Yamaha", "MT-07", 10000)
truck1 = Truck("Volvo", 'FH16', 15000)

#clientes
cliente1 = Customer("Juan Daniel")

#Tienda
tienda1 = Dealership()

#agregamos vehiculos a la tienda
tienda1.add_vehicles(car1)
tienda1.add_vehicles(bike1)
tienda1.add_vehicles(truck1)

#agegamos cliente a la tienda
tienda1.register_customers(cliente1)

#Mostrar vehiculos diponibles
tienda1.show_available_vehicles()

#Cliente consulta por la disponibilidad de un vehiculo
cliente1.inquiere_vehicle(bike1)

#El cliente quiere comprar un vehiculo
cliente1.buy_vehicle(bike1)

#Mostrar vehiculos diponibles
tienda1.show_available_vehicles()