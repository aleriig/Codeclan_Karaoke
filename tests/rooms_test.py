import unittest
from classes.rooms import Rooms
from classes.songs import Songs
from classes.guests import Guests
from classes.bar import Bar

class TestRooms(unittest.TestCase):

    def setUp(self):
        self.rooms_1 = Rooms(1, 2, "Sympathy for the Devil", 10.00)
        self.rooms_2 = Rooms(2, 4, "Under Pressure",15.00)
        self.rooms_3 = Rooms(3, 3, "La Macarena", 13.00)
        self.guests_1 = Guests("Brian Robinson", 50.00, "La Macarena")
        self.guests_2 = Guests("Luke Shaw", 22.30, "Sympathy for the Devil")
        self.songs_1 = Songs("La Macarena")
        self.songs_2 = Songs("Sympathy for the Devil")
        self.songs_3 = Songs("Under Pressure")
        self.bar = Bar(20.00)

        
    def test_rooms_has_a_number(self):
        self.assertEqual(1, self.rooms_1.number)

    def test_rooms_add_guest(self):
        self.rooms_1.add_guest(self.guests_1)
        self.assertEqual(1, self.rooms_1.guest_count())

    def test_rooms_remove_guest(self):
        self.rooms_1.add_guest(self.guests_1)
        self.rooms_1.add_guest(self.guests_2)
        self.rooms_1.remove_guest(self.guests_1)
        self.assertEqual(1, self.rooms_1.guest_count())

    def test_add_songs_to_rooms(self):
        self.rooms_1.add_song(self.rooms_1)
        self.assertEqual(1, self.rooms_1.song_count())

    def test_capacity_room(self):
        self.rooms_2.add_guest(self.guests_1)
        self.rooms_2.add_guest(self.guests_2)
        self.rooms_2.full_room(self.rooms_2)
        self.assertEqual(4, self.rooms_2.capacity)

    def test_this_is_my_favourite_song(self):
        self.rooms_3.add_guest(self.guests_1)
        self.rooms_3.favourite_song(self.rooms_3)
        self.assertEqual("La Macarena", self.guests_1.song)

    def test_track_spent_money(self):
        self.rooms_1.add_guest(self.guests_1)
        self.rooms_1.add_guest(self.guests_2)
        self.rooms_1.entry_fee(self.rooms_1.fee)
        self.assertEqual(20, self.bar.till)
        