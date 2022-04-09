class Guests:
    def __init__(self, name, wallet):
        self.name = name 
        self.wallet = wallet

    def entry_fee(self, ticket):
        self.wallet -= ticket
