from deck import deck
from hand import hand

def main():
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

        if player.handValue == 21:
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
                
                if player.handValue > 21:
                    print("You Busted!")
                    playerHit = False
                    playerEndGame = True
                elif player.handValue == 21:
                    print("You win!!")
                    playerHit = False
                    playerEndGame = True

        dealerEndGame = False    
        if not playerEndGame:
            dealerHit = True
            while dealerHit:
                print("Here are the dealer's cards:")
                dealer.displayHand()
                if dealer.handValue == 21:
                    print("The dealer wins!")
                    dealerHit = False
                    dealerEndGame = True
                elif dealer.handValue > 21:
                    print("You win!")
                    dealerHit = False
                    dealerEndGame = True
                elif dealer.handValue >= 17:
                    dealerHit = False
                elif dealer.handValue < 17:
                    dealer.hit(d)
                    dealerHit = True
                    
            if not dealerEndGame:
                if player.handValue > dealer.handValue:
                    print("You win!")
                elif player.handValue == dealer.handValue:
                    print("You push!")
                else: 
                    print("You Lose!")

        again = input('Pla(y) agai(n)?: ')
        
        if again == 'n':
            break

if __name__ == '__main__':
    main()
