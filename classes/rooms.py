from classes.guests import Guests
from classes.bar import Bar


class Rooms:
    def __init__(self, number, capacity, song_availabe, fee):
        self.number = number
        self.capacity = capacity
        self.song_available = song_availabe
        self.fee = fee
        self.guests = []
        self.songs = []
        self.till = []

    def guest_count(self):
         return len(self.guests)

    def add_guest(self, guest):
        self.guests.append(guest)

    def remove_guest(self, guest):
         self.guests.remove(guest)
        
    def song_count(self):
        return len(self.songs)

    def add_song(self, song):
         self.songs.append(song)

    def full_room(self, guest):
        if self.guests.count(guest) == self.capacity:
            return "This room is full"
        else:    
            return "You can enter"

    def favourite_song(self, song):
        if song == self.song_available:
            return "Whoooooooo!!!"    
        else:
            return "Oh no! I don't like this song!"

    def entry_fee(self, till):
        self.fee += till

    