import unittest
from classes.bar import Bar
from classes.drinks import Drinks
from classes.guests import Guests

class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar(20.00)
        self.drink_1 = ("Water", 2.50)
        self.drink_2 = ("Rhum", 7.80)
        self.drink_3 = ("Beer", 5.20)
        self.guests_1 = Guests("Brian Robinson", 50.00, "La Macarena")

    def test_bar_has_a_till(self):
        self.assertEqual(20.00, self.bar.till)

    def test_add_drink(self):
        self.bar.add_drink(self.drink_1)

    def test_bar_earning_money(self):
        self.bar.add_drink(self.drink_1)
        self.bar.selling_drinks(self.guests_1, self.drink_1)
        self.assertEqual(47.50, self.guests_1.wallet)
        self.assertEqual(22.50, self.bar.till)

