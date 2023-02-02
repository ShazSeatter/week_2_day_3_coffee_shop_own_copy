import unittest 
from src.customer import Customer
from src.drinks import Drinks
# from src.food import Food

class TestCustomer(unittest.TestCase):  
    def setUp(self): 

        self.customer = Customer("John Snow", 50, 30, 3)
        self.drink_4 = Drinks("Latte", 15, 2)
    
    def test_has_name_of_customer(self):
        self.assertEqual("John Snow", self.customer.name)

    def test_has_customer_got_money(self):
        self.customer.can_buy_drink(self.drink_4)
        self.assertEqual(50, self.customer.wallet)

    
    def test_reduce_amount_in_wallet(self):
        self.customer.reduce_wallet_amount(10)
        self.assertEqual(40, self.customer.wallet)


    def test_energy_level(self):
        self.customer.change_energy_level(self.drink_4.caffeine_level)
        self.assertEqual(5, self.customer.energy_level)

    
