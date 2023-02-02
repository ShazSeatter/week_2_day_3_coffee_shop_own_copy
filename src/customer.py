
class Customer: 
    def __init__(self, name, wallet, age, energy_level):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.energy_level = energy_level #1-5


    def reduce_wallet_amount(self, amount):
        self.wallet -= amount 


    # def can_buy_drink(self, drink):
    
    def change_energy_level(self, caffeine_level):
        self.energy_level += caffeine_level