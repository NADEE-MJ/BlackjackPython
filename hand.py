from card import card

class hand():
    def __init__(self):
        self.hand = []
        self.valueHand = self.handValue()

    def clearHand(self):
        self.hand = []
        
    def dealHand(self, deck):
        standardHand = 2

        for i in range(standardHand):
            self.hand.append(card(deck.cardPile[deck.topCard].value, deck.cardPile[deck.topCard].suit))
            deck.topCard += 1

    def hit(self, deck):
        self.hand.append(card(deck.cardPile[deck.topCard].value, deck.cardPile[deck.topCard].suit))
        deck.topCard += 1

    def handValue(self):
        handValue = 0
        for handCard in self.hand:
            cardValue = handCard.cardValue()
            if cardValue == 1:
                if (handValue + 11) > 21:
                    handValue += 1
                else:
                    handValue += 11
            else:
                handValue += cardValue
                
        return handValue

    def displayHand(self):
        for handCard in self.hand:
            temp = handCard.displayCardName()
            for i in range(len(temp), 21):
                temp += " "
            print(temp)

        self.valueHand = self.handValue()
        print("Hand value is " + str(self.valueHand))