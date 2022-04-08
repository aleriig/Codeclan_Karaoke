import unittest
from classes.guests import Guests

class TestGuests(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guests("Brian Robinson")
        self.guests_2 = Guests("Luke Shaw")
        
    def test_guest_has_a_name(self):
        self.assertEqual("Brian Robinson", self.guest_1.name)   
