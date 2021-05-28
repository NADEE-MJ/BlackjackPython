from card import card
import random

class deck(card):
    topCard = 0
    deck = []

    def __init__(self, topCard):
        self.topCard = topCard
        self.createDeck()
        self.shuffle()

    def createDeck(self):
        cardsInSuit = 13
        numberOfSuits = 4
        for i in numberOfSuits:
            for j in range(cardsInSuit):
                self.deck.append(card(j+1, 'D'))
            for j in range(cardsInSuit):
                self.deck.append(card(j+1, 'H'))
            for j in range(cardsInSuit):
                self.deck.append(card(j+1, 'S'))
            for j in range(cardsInSuit):
                self.deck.append(card(j+1, 'C'))

    def shuffle(self):
        perfectShuffle = 7
        cardsInDeck = 52
        temp = card(0, 'D')

        random.seed()
        for i in range(perfectShuffle):
            for j in range(cardsInDeck):
                r = random.randint() % (cardsInDeck - i) + i

                temp = self.deck[i]
                self.deck[i] = self.deck[r]
                self.deck[r] = temp
