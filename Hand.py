from card import card

class hand(card):
    hand = []
    sizeHand = 0
    valueHand = 0

    def __init__(self, sizeHand, valueHand):
        self.sizeHand = sizeHand
        self.valueHand = valueHand
        createHand()

    def createHand(self):
        largestHand = 11

        for i in range(largestHand):
            self.hand.append(card(0, ' '))

    def dealHand()
    def hit()
    def handValue()
    def displayHand()