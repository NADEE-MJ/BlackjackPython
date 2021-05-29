from card import card
import random

class deck():
    def __init__(self):
        self.cardPile = []
        self.createDeck()
        self.shuffle()
        
    def createDeck(self):
        cardsInSuit = 13
        for i in range(1,cardsInSuit+1):
            self.cardPile.append(card(i, 'D'))
            self.cardPile.append(card(i, 'H'))
            self.cardPile.append(card(i, 'S'))
            self.cardPile.append(card(i, 'C'))

    def shuffle(self):
        self.topCard = 0
        random.shuffle(self.cardPile)
