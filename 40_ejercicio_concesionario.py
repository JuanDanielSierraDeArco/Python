# ejercicio del concecionario

class vehiculos:
    def __init__(self, auto, precio):
        self.auto = auto
        self.precio = precio
        self.disponible = True

    def sell(self):
        if self.disponible:
            self.disponible = False
            print('El automovil {} ha sido vendido con precio {}'.format(self.auto, self.precio))
        else:
            print('El automovil {} no esta disponible para venta')

    def check_availability(self):
        return self.disponible
    
    def get_prece(self):
        return self.precio

class customer:
    def __init__(self, name):
        self.name = name
        self.cars_purchased = []
    
    def buy_car(self, vehiculos):
        if vehiculos.check_availability():
            vehiculos.sell()
            self.cars_purchased.append(vehiculos)

        else:
            print('El automovil {} no esta disponible'.format(vehiculos.auto))
    
    def inquiere_car(self, vehiculos):
        availability = 'Disponible' if vehiculos.check_availability() else 'No disponible'
        print('El automivil {} esta {} y tiene un precio de {}'.format(vehiculos.auto, availability, vehiculos.precio))

class dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []
    
    def add_car(self, vehiculos):
        self.inventory.append(vehiculos)
        print('El automivil {} ha sido agregado al inventario.'.format(vehiculos.auto))

    def register_customer(self, customer):
        self.customers.append(customer)
        print('El cliente {} ha sido registrado en la concesionaria'.format(customer.name))
    
    def show_vailable_cars(self):
        print('Coches disponibles en la concesionaria')
        for vehiculos in self.inventory:
            if vehiculos.check_availability():
                print('- {} por valor {}'.format(vehiculos.auto, vehiculos.get_prece()))


#Crear instancias de coches

car1 = vehiculos('Corolla', '20000')
car2 = vehiculos('Prado', '40000')
car3 = vehiculos('Mustang', '80000')

#Crear instancias de coches 
customer1 = customer('Ana Arroyo')

#Crear instancia de concesionaria y registrar coche y clientes
dealership = dealership()
dealership.add_car(car1)
dealership.add_car(car2)
dealership.add_car(car3)
dealership.register_customer(customer1)

#Mostrar coches disponible

dealership.show_vailable_cars()

#Cliente consulta uin coche
customer1.inquiere_car(car1)

#clinte compra un coche
customer1.buy_car(car1)

#Mostrar coches disponible
dealership.show_vailable_cars()

#clinte compra un coche
customer1.buy_car(car1)