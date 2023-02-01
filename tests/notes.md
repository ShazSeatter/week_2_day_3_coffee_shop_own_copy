import unittest 
from src.coffee_shop import CoffeeShop

# Using this as a template
# Test goes at the beginning
# need to have unittest.TestCase in the parameters

class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        # want a coffee shop object so we can access and check 
        # it will set back to its original state before each test
        # self. creating a property as part of the Test Class
        self.coffee_shop = CoffeeShop("The Prancing Pony", 100.00)

# need to start with test_
# testing what the class should be 
    def test_has_name(self):
        # special method that takes in 2 values, expect, what you get back
        # they need to be the same
        # when we access the coffee shop name, we are checking that we get the " " back
        #  always want to run tests and expect it to fail
        self.assertEqual("The Prancing Pony", self.coffee_shop.name)


    def test_has_till(self):
        self.assertEqual(100.00, self.coffee_shop.till)

    
    def test_increase_till(self):
        # The 3 A's of Testing 
        # Arrange - set up that needs to be done specific to this test
        # Act - do the thing you want to test, 1 thing

        self.coffee_shop.increase_till(10.00)
        # giving the method an argument to pass in 

        # Assert - did it do what you wanted?
        #  expect the coffee shop till attribute to be 110 
        self.assertEqual(110.00, self.coffee_shop.till)