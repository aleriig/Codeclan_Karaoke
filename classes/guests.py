class Guests:
    def __init__(self, name, wallet, song):
        self.name = name 
        self.wallet = wallet
        self.song = song

    def less_money(self, ticket):
        self.wallet -= ticket

       
        
