class Bar:
    def __init__(self, till):
        self.till = till
        self.drinks = []

    def add_drink(self):
        return len(self.drinks)

    def selling_drinks(self, guests, drink):
        guests.buy_drink(drink)
        self.till += drink.price
    





        