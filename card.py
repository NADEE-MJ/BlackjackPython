# This is the card class
class card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def displayCardName(self):
        faces = {1:'Ace', 11:'Jack', 12:'Queen', 13:'King'}
        suits = {'D': 'Diamonds', 'H': 'Hearts', 'S': 'Spades', 'C':'Clubs'}
        cardName = '['

        if (self.value > 1 and self.value <= 10):
            cardName += str(self.value)
        else:
            cardName += faces[self.value]
        
        cardName += ' of ' + suits[self.suit] + ']'
        return cardName

    def cardValue(self):
        if (self.value <= 10):
            return self.value
        else:
            return 10