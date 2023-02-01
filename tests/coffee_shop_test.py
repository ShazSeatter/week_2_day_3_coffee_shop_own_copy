import unittest 
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.drinks import Drinks



class TestCoffeeShop(unittest.TestCase):
    def setUp(self):

        self.drink_1 = Drinks("Hot Chocolate", 20, 1)
        self.drink_2 = Drinks("Espresso", 10, 3)
        self.drink_3 = Drinks("Latte", 15, 2)

        drinks = [self.drink_1, self.drink_2, self.drink_3]

        
        self.coffee_shop = CoffeeShop("The Prancing Pony", 100.00, drinks)
        
        self.customer = Customer("John Snow", 50, 30, 3)
    
    def test_has_name(self):
        self.assertEqual("The Prancing Pony", self.coffee_shop.name)


    def test_has_till(self):
        self.assertEqual(100.00, self.coffee_shop.till)

    
    def test_increase_till(self):
        self.coffee_shop.increase_till(10.00)
        self.assertEqual(110.00, self.coffee_shop.till)


    def test_has_drink(self):
        self.assertEqual(3, len(self.coffee_shop.drinks))


    def test_find_drink_in_coffe_store(self): 
        found_drink = self.coffee_shop.find_drink("Espresso")
        self.assertEqual(self.drink_2, found_drink)


    def test_remove_drinks_if_sold(self):
        self.coffee_shop.remove_drink(self.drink_3)
        self.assertEqual(2, len(self.coffee_shop.drinks))


    def test_check_age_of_customer__True(self):
        self.assertEqual(True, self.customer.age > 16)


    def test_check_age_of_customer__False(self):
        self.customer_2 = Customer("Jane Doe", 40, 14, 2)
        self.coffee_shop.check_age(self.customer_2.age)
        self.assertEqual(False, self.customer_2.age > 16)
    


    # def test_check_age_of_customer__False(self):
    #     self.customer_2 = Customer("John Doe", 40, 14)
    #     self.coffee_shop.check_age_of_customer(self.customer_2.age)
    #     self.assertEqual(False, self.customer.age)

    def test_sell_drink_to_customer__1(self):
        self.coffee_shop.sell_drink_to_customer(self.drink_3, self.customer)
        self.assertEqual(30, self.customer.age)
        self.assertEqual(2, len(self.coffee_shop.drinks))
        self.assertEqual(115.00, self.coffee_shop.till)
        self.assertEqual(35, self.customer.wallet)
       

    def test_sell_drink_to_customer__2(self):
        self.customer_3 = Customer("Jane Smith", 40, 14, 2)
        self.assertEqual(None, self.coffee_shop.sell_drink_to_customer(self.drink_3, self.customer_3))
        self.assertEqual(14, self.customer_3.age)
        self.assertEqual(3, len(self.coffee_shop.drinks))
        self.assertEqual(100.00, self.coffee_shop.till)
        self.assertEqual(40, self.customer_3.wallet)

