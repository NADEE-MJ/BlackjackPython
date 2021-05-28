# This is the card class
class card:
    value = 0
    suit = ''

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def displayCardName(self):
        # cardName = "["

        # if (self.value > 1 and self.value <= 10):
        #     cardName += self.value
        # else:
        #     if (self.value == 1):
        #         cardName += "Ace"
        #     elif (self.value == 11):
        #         cardName += "Jack"
        #     elif (self.value == 12):
        #         cardName += "Queen"
        #     elif (self.value == 13):
        #         cardName += "King"
        
        # cardName += " of "

        # if (self.suit == 'D'):
        #     cardName += "Diamonds"
        # elif (self.suit == 'H'):
        #     cardName += "Hearts"
        # elif (self.suit == 'S'):
        #     cardName += "Spades"
        # elif (self.suit == 'C'):
        #     cardName += "Clubs"

        faces = {1:'Ace', 11:'Jack', 12:'Queen', 13:'King'}
        suits = {'D': 'Diamonds', 'H': 'Hearts', 'S': 'Spades', 'C':'Clubs'}
        cardName = '['

        if (self.value > 1 and self.value <= 10):
            cardName += self.value
        else:
            cardName += faces[self.value]
        
        cardName += ' of '

        cardName += suits[self.suit]

        



    def cardValue(self):
        if (self.value <= 10):
            return self.value
        else:
            return 10
