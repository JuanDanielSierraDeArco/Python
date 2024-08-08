print('---------------Bienvenido--------')

class vehicle:
    def __init__(self, brand, model, price):
        # Encapsulación
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print('El vehiculo {} ha sido vendido'.format(self.brand))
        
        else:
            print('El vehiculo {} no esta disponible'.format(self.brand))
 #Abstracción
    def check_available(self):
        return self.is_available
  #Abstracción   
    def get_price(self):
        return self.price
    #Polimorfismo
    def star_engine(self):
        raise NotImplementedError('Este metDealership.add_vehicles(car1)odo debe ser implementado por la subclase')
    
    #Polimorfismo
    def stop_engine(self):
        raise NotImplementedError('Este metodo debe ser implementado por la subclase')
#Herencia
class Car(vehicle):
    #Polimorfismo    
    def star_engine(self):
        if not self.is_available:
            return 'El conche {} esta en marcha'.format(self.brand)
                
        else:
            return 'El coche {} no esta disponible'.format(self.brand) 
    #Polimorfismo           
    def stop_enegine(self):
        if self.is_available:
            return 'El motor del coche {} se ha detenido'.format(self.brand)
                
        else:
            return 'El coche {} no esta disponible'.format(self.brand)
 #Herencia               
class Bike(vehicle):
    #Polimorfismo
    def star_engine(self):
        if not self.is_available:
            return 'La bicicleta {} esta en marcha'.format(self.brand)
                
        else:
            return 'La bicicleta {} no esta disponible'.format(self.brand) 
           
    def stop_enegine(self):
        if self.is_available:

            return 'La bicicleta {} se ha detenido'.format(self.brand)
            
        else:
            return 'La bicicleta {} no esta disponible'.format(self.brand)
#Herencia
class Truck(vehicle):
    #Polimorfismo
    def star_engine(self):
        if not self.is_available:
            return 'El motort del camion {} esta en marcha'.format(self.brand)
                
        else:
            return 'El  camion {} no esta disponible'.format(self.brand) 
    #Polimorfismo      
    def stop_enegine(self):
        if self.is_available:

            return 'El motort del camion {} se ha detenido'.format(self.brand)
            
        else:
            return 'El camion {} no esta disponible'.format(self.brand)

class customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []
    
    def buy_vehicle(self, vehicle: vehicle):
        if vehicle.check_available:
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        
        else:
            print('Lo siento, {} no esta disponible'.format(vehicle.brand))
    def inquiere_vehicle(self, vehicle: vehicle):
        if vehicle.check_available():
            available = 'Disponible'
        else:
            available = 'No disponible'
        print('El {} esta {} y cuesta {}'.format(vehicle.brand, available, vehicle.get_price()))

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicle: vehicle):
        self.inventory.append(vehicle)
        print('El vehiculo {} ha sido añadido al invetary'.format(vehicle.brand))
    
    def register_customers(self, customer: customer):
        self.customers.append(customer)
        print('El cliente {} ha sido añadido'.format(customer.name))

    def show_available_vehicle(self):
        print('vehiculos disponibles')
        for vehicle in self.inventory:
            if vehicle.check_available():
                print('- {} por valor  {}'.format(vehicle.brand, vehicle.get_price()))

#Crear instancias de coches
car1 = Car('Toyota', 'Corolla', '20000')
bike1 = Bike('Yamaha', 'MT-07', '32000')
Truck1 = Truck('Volvo', 'FH16', '80000')

#Crear instancias de CUSTOMERS
customer1 = customer('Juan Daniel')

Dealership = Dealership()
Dealership.add_vehicles(car1)
Dealership.add_vehicles(bike1)
Dealership.add_vehicles(Truck1)

Dealership.register_customers(customer1)

#Mostrar vehiculos disponible
Dealership.show_available_vehicle()

customer1.inquiere_vehicle(car1)

customer1.buy_vehicle(car1)

Dealership.show_available_vehicle()


'''
Encapsulamiento:* Agrupa datos y métodos relacionados en una clase.
Oculta los detalles internos y controla el acceso a los datos.
Ejemplo: Una clase "Coche" que encapsula propiedades como "color" y métodos como "arrancar".
Abstracción:* Simplifica sistemas complejos ocultando detalles innecesarios.
Permite centrarse en las características esenciales de un objeto.
Ejemplo: Una interfaz "Vehículo" con método "mover", sin especificar cómo se implementa.
Herencia:* Permite que una clase (hija) herede propiedades y métodos de otra (padre).
Promueve la reutilización de código y la jerarquía de clases.
Ejemplo: "Coche" y "Moto" heredan de "Vehículo".
Polimorfismo:* Permite que objetos de diferentes clases respondan al mismo método de manera única.
Facilita el uso de una interfaz común para tipos de datos diversos.
Ejemplo: Diferentes tipos de "Vehículo" implementan el método "mover" de forma distinta.
'''