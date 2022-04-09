import unittest
from classes.guests import Guests

class TestGuests(unittest.TestCase):

    def setUp(self):
        self.guests_1 = Guests("Brian Robinson", 50.00)
        self.guests_2 = Guests("Luke Shaw", 22.30)
        
    def test_guest_has_a_name(self):
        self.assertEqual("Brian Robinson", self.guests_1.name)

    def test_guest_has_a_wallet(self):
        self.assertEqual(22.30, self.guests_2.wallet) 

    def test_guest_has_pay_entry_fee(self):
        self.guests_1.entry_fee(8.00)
        self.assertEqual(42.00, self.guests_1.wallet)