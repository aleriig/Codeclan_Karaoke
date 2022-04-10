import unittest
from classes.drinks import Drinks

class TestDrinks(unittest.TestCase):
    def setUp(self):
        self.drinks = Drinks("Water", 2.50)

    def drink_has_a_name(self):
        self.assertEqual("Water", self.drinks.name)

    def drink_has_a_price(self):
        self.assertEqual(2.50, self.drinks.price)