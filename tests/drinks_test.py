import unittest 
from src.drinks import Drinks

class TestCustomer(unittest.TestCase):  
    def setUp(self): 

        self.drink = Drinks("Cappunico", 30, 2)

    def test_drink_has_name(self):
        self.assertEqual("Cappunico", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(30, self.drink.price)
    
    def test_drink_caffine_level(self):
        self.assertEqual(2, self.drink.caffeine_level)