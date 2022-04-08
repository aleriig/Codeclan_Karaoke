class Rooms:
    def __init__(self, number):
        self.number = number
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