
class BankAccount:
    
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print('se ha depositado {}. Saldo actual => {}'.format(amount, self.balance))
        else:
            print('no se puede depositar cuenta inactiva')

    def withdraw(self, amount):
        if self.is_active:
            self.balance -= amount
            print('se ha retirado {}. Saldo actual => {}'.format(amount, self.balance))

    def desactive_account(self):
        self.is_active = False
        print('La cuenta ha sido desactivada')

    def activate_account(self):
        self.is_active = True
        print('La cuenta ha sido activada')



account1 = BankAccount('juan', 500)
account2 = BankAccount('ana', 1000)

#Llamando a los metodos

account1.deposit(300)
account2.deposit(400)

account1.desactive_account()
account1.deposit(500)

account1.activate_account()
account1.deposit(500)