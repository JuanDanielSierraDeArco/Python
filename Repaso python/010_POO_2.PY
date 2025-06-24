#Ejercicio cuenta de banco

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

#depositar
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado en la cuenta {amount}. en saldo actual es {self.balance}")
        else:
            print("No se puede depositar la cuenta esta inactiva")

#retirar dinero
    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado de la cuenta {amount}. el saldo actual es {self.balance}")
            else:
                print("Saldo insuficiente el valaor a retitar es mayor que su sado actual")
        else: 
            print("No se pued retirar, la cuenta esta inactiva")
#desactivar cuenta
    def deactivate_account(self):
        self.is_active = False
        print("La cuenta ha sido desactivada")
    
#actvar cuenta
    def activate_account(self):
        self.is_active = True
        print("La cuenta ha sido activada")


persona1 = BankAccount('Juan', 1000)
persona2 = BankAccount('Daniel', 500)

persona1.deposit(1000)
persona2.withdraw(700)

persona1.deactivate_account()
persona1.withdraw(500)
persona1.activate_account()
persona1.withdraw(500)