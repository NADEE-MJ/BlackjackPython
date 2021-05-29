from deck import deck
from hand import hand

d = deck()

player = hand()
dealer = hand()

while True:
    player.clearHand()
    dealer.clearHand()
    print("Game: Blackjack\n\nHere are your cards:")

    player.dealHand(d)
    player.displayHand()
    dealer.dealHand(d)

    if player.valueHand == 21:
        print("You Win!")
        playerEndGame = True
    else:
        playerHit = True
        while playerHit:
            hitOrStay = input("Would you like to (h)it or (s)tay?: ")
            if hitOrStay == 'h':
                player.hit(d)
                player.displayHand()
            else:
                playerHit = False
                playerEndGame = False
            if player.valueHand > 21:
                print("You Busted!")
                playerHit = False
                playerEndGame = True
            elif player.valueHand == 21:
                print("You win!!")
                playerHit = False
                playerEndGame = True

    dealerEndGame = False    
    if not playerEndGame:
        dealerHit = True
        while dealerHit:
            print("Here are the dealer's cards:")
            dealer.displayHand()
            if dealer.valueHand == 21:
                print("THe dealer wins!")
                dealerHit = False
                dealerEndGame = True
            elif dealer.valueHand > 21:
                print("You win!")
                dealerHit = False
                dealerEndGame = True
            elif dealer.valueHand >= 17:
                dealerHit = False
            elif dealer.valueHand < 17:
                dealer.hit(d)
                dealerHit = True
                
        if not dealerEndGame:
            if player.valueHand > dealer.valueHand:
                print("You win!")
            elif player.valueHand == dealer.valueHand:
                print("You push!")
            elif player.valueHand < dealer.valueHand:
                print("You Lose!")

    again = input('Pla(y) agai(n)?: ')
    
    if again == 'n':
        break