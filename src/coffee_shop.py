

class CoffeeShop:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till 
        self.drinks = drinks

    def increase_till(self, amount):
        self.till += amount


    def find_drink(self, order):
        for drink_in_shop in self.drinks:
            if drink_in_shop.name == order:
                return drink_in_shop

    def remove_drink(self, drink):
        self.drinks.remove(drink)

    def check_age(self, customer):
        if customer > 16:
            return True
        else:
            return False 

    def sell_drink_to_customer(self, drink, customer):
        found_drink = self.find_drink(drink.name)
        if found_drink == drink and self.check_age(customer.age):
            self.remove_drink(drink)
            self.increase_till(drink.price)
            customer.reduce_wallet_amount(drink.price)
        else:
            return None
\

