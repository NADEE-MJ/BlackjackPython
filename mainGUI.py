import pygame, sys
from deck import deck
from hand import hand
from cardGUI import cardGUI
from pygame.constants import K_SPACE

def quitCheck():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def main():
    pygame.init()

    #fps settings
    FPS = 60
    FramePerSec = pygame.time.Clock()

    #screen settings
    screen = pygame.display.set_mode([1000, 500])
    pygame.display.set_caption("Blackjack")
    font = pygame.font.Font(pygame.font.get_default_font(), 20)

    #colors
    black = (0, 0, 0)
    green = (0, 128, 0)

    #setting fonts
    text = font.render("Dealer's Cards", True, black)

    hit = False
    begin = False
    #main game loop
    while True:
        quitCheck()
        
        screen.fill(green)  

        font = pygame.font.Font(pygame.font.get_default_font(), 125)
        title = font.render("BLACKJACK!", True, black)
        titleSurface = pygame.Surface((200, 100))
        titleRect = titleSurface.get_rect(center = (200, 250))
        screen.blit(title, titleRect)

        font = pygame.font.Font(pygame.font.get_default_font(), 25)
        title = font.render("Press [SPACE] to begin...", True, black)
        titleSurface = pygame.Surface((200, 100))
        titleRect = titleSurface.get_rect(center = (250, 400))
        screen.blit(title, titleRect)

        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_SPACE]:
            print("Hello")
        if begin:
            screen.fill(green)
            d = deck()

            player = hand()
            dealer = hand()

            player.clearHand()
            dealer.clearHand()

            player.dealHand(d)
            dealer.dealHand(d)

            playerCards = player.cardIDs()
            #dealerCards = dealer.cardIDs()

            playerCardsGUI= []
            for ID in playerCards:
                playerCardsGUI.append(cardGUI(ID))
            
            distanceToRight = 100
            for card in playerCardsGUI:
                card.draw(screen, distanceToRight)
                distanceToRight += 150

            pygame.display.update()
            while True:
                quitCheck()
      
        elif pressed_key[K_SPACE]:
            begin = True

        pygame.display.update()
        FramePerSec.tick(FPS)
        

    # d = deck()
    # player = hand()
    # dealer = hand()



    # while True:
    #     player.clearHand()
    #     dealer.clearHand()
    #     print("Game: Blackjack\n\nHere are your cards:")

    #     player.dealHand(d)
    #     player.displayHand()
    #     dealer.dealHand(d)

    #     if player.valueHand == 21:
    #         print("You Win!")
    #         playerEndGame = True
    #     else:
    #         playerHit = True
    #         while playerHit:
    #             hitOrStay = input("Would you like to (h)it or (s)tay?: ")
    #             if hitOrStay == 'h':
    #                 player.hit(d)
    #                 player.displayHand()
    #             else:
    #                 playerHit = False
    #                 playerEndGame = False
    #             if player.valueHand > 21:
    #                 print("You Busted!")
    #                 playerHit = False
    #                 playerEndGame = True
    #             elif player.valueHand == 21:
    #                 print("You win!!")
    #                 playerHit = False
    #                 playerEndGame = True

    #     dealerEndGame = False    
    #     if not playerEndGame:
    #         dealerHit = True
    #         while dealerHit:
    #             print("Here are the dealer's cards:")
    #             dealer.displayHand()
    #             if dealer.valueHand == 21:
    #                 print("THe dealer wins!")
    #                 dealerHit = False
    #                 dealerEndGame = True
    #             elif dealer.valueHand > 21:
    #                 print("You win!")
    #                 dealerHit = False
    #                 dealerEndGame = True
    #             elif dealer.valueHand >= 17:
    #                 dealerHit = False
    #             elif dealer.valueHand < 17:
    #                 dealer.hit(d)
    #                 dealerHit = True
                    
    #         if not dealerEndGame:
    #             if player.valueHand > dealer.valueHand:
    #                 print("You win!")
    #             elif player.valueHand == dealer.valueHand:
    #                 print("You push!")
    #             elif player.valueHand < dealer.valueHand:
    #                 print("You Lose!")

    #     again = input('Pla(y) agai(n)?: ')
        
    #     if again == 'n':
    #         break

main()