import unittest 
from src.customer import Customer

class TestCustomer(unittest.TestCase):  
    def setUp(self): 

        self.customer = Customer("John Snow", 50, 30)

    
    def test_has_name_of_customer(self):
        self.assertEqual("John Snow", self.customer.name)

    def test_has_customer_got_money(self):
        self.assertEqual(50, self.customer.wallet)


    def test_reduce_amount_in_wallet(self):
        self.customer.reduce_wallet_amount(10)
        self.assertEqual(40, self.customer.wallet)


    