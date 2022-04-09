from tokenize import Number


class Rooms:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = []
        self.songs = []

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
        