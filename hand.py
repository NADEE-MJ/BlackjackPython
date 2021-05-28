from card import card

class hand(card):
    hand = []
    sizeHand = 0
    valueHand = 0

    def __init__(self, sizeHand, valueHand):
        self.sizeHand = sizeHand
        self.valueHand = valueHand
        self.createHand()

    def createHand(self):
        largestHand = 11

        for i in range(largestHand):
            self.hand.append(card(0, ' '))

    def dealHand(self, deck, topCard):
        standardHand = 2
        self.sizeHand = standardHand

        for i in range(standardHand):
            self.hand[i] = deck[topCard]
            topCard += 1

    def hit(self, deck, topCard):
        self.hand[self.sizeHand] = deck[topCard]
        topCard += 1
        self.sizeHand += 1

    def handValue(self):
        handValue = 0
        for i in self.sizeHand:
            cardValue = self.hand[i].cardValue()
            if cardValue >= 2:
                handValue += cardValue
            elif cardValue== 1:
                if (handValue + 11) > 21:
                    handValue += 1
                else:
                    handValue += 1
        return handValue

    def displayHand(self):
        textCardSize = 13
        temp = ""

        for i in range(self.sizeHand):
            temp = self.hand[i].displayCardName()
            for j in range(len(temp), 21):
                temp += " "
            print(temp)

        valueHand = self.handValue()
        print("Hand value is " + valueHand)
