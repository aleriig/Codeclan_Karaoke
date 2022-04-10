import unittest
from classes.songs import Songs

class TestSongs(unittest.TestCase):

    def setUp(self):
        self.songs_1 = Songs("La Macarena")
        
    def test_song_has_a_name(self):
        self.assertEqual = ("La Macarena", self.songs_1.name)