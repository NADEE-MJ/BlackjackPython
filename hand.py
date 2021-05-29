from card import card

class hand():
    def __init__(self):
        self.hand = []
        self.handValue = self.getHandValue()

    def clearHand(self):
        self.hand = []
        
    def hit(self, deck):
        self.hand.append(card(deck.cardPile[deck.topCard].value, deck.cardPile[deck.topCard].suit))
        deck.topCard += 1
        self.handValue = self.getHandValue()
    
    def dealHand(self, deck):
        standardHand = 2

        for i in range(standardHand):
            self.hit(deck)
        self.handValue = self.getHandValue()
    
    def getHandValue(self):
        handValue = 0
        hasAce = False
        for handCard in self.hand:
            cardValue = handCard.cardValue()
            if cardValue == 1:
                if hasAce:
                    handValue += 1
                else:
                    handValue += 11
                    hasAce = True
            else:
                handValue += cardValue
        
        if hasAce and handValue > 21:
            handValue -= 10
        return handValue

    def displayHand(self):
        for handCard in self.hand:
            temp = handCard.displayCardName()
            for i in range(len(temp), 21):
                temp += " "
            print(temp)

        print("Hand value is " + str(self.handValue))

    def cardIDs(self):
        cardIDs = [handCard.cardID() for handCard in self.hand]
        return cardIDs
            
