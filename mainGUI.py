import pygame, sys, time
from deck import deck
from hand import hand
from cardGUI import cardGUI
from pygame.constants import K_SPACE, K_h, K_s, K_y, K_n
from pygame.locals import *

def displayGUICards(cardIDs, screen, distanceToBottom):
    cardsGUI= []
    for ID in cardIDs:
        cardsGUI.append(cardGUI(ID))
            
    distanceToRight = 100
    for card in cardsGUI:
        card.draw(screen, distanceToRight, distanceToBottom)
        distanceToRight += 150

def displayText(screen, color, backgroundColor, output, size, position):
    font = pygame.font.Font(pygame.font.get_default_font(), size)
    text = font.render(output, True, color, backgroundColor)
    surface = pygame.Surface((200, 100))
    rect = surface.get_rect(center = position)
    screen.blit(text, rect)

def twoButton(butt1, butt2):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == butt1:
                return True
            elif event.type == KEYDOWN and event.key == butt2:
                return False

def oneButton(butt1):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == butt1:
                        return True

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
    red = (128, 0, 0)
    black = (0, 0, 0)
    green = (39, 91, 1)

    #setting fonts
    text = font.render("Dealer's Cards", True, black)

    d = deck()

    player = hand()
    dealer = hand()
    
    #main game loop
    while True:
        
        screen.fill(green)  

        displayText(screen, black, green, "BLACKJACK!", 125, (200, 250))

        displayText(screen, black, green, "Press [SPACE] to begin...", 25, (250, 400))

        pygame.display.update()

        if oneButton(K_SPACE):
            screen.fill(green)
            
      
            #show player cards
            player.clearHand()
            player.dealHand(d)
            playerCardIDs = player.cardIDs()
            player.handValue = player.getHandValue()

            displayGUICards(playerCardIDs, screen, 375)
            
            dealer.clearHand()
            dealer.dealHand(d)
            dealerCardIDs = dealer.cardIDs()

            dealerCardsGUI= []
            for ID in dealerCardIDs:
                dealerCardsGUI.append(cardGUI(ID))
            
            distanceToRight = 100
            screen.blit(dealerCardsGUI[1].cardBack, dealerCardsGUI[0].surf.get_rect(center = (distanceToRight, 125)))
            distanceToRight += 150
            dealerCardsGUI[1].draw(screen, distanceToRight, 125)
                
            pygame.display.update()

            while True:
                player.handValue = player.getHandValue() # TODO
                if player.handValue == 21:
                    time.sleep(0.5)
                    displayText(screen, black, red, "You Win!", 125, (200, 250))
                    playerEndGame = True
                    pygame.display.update()
                else:
                    while True:
                        
                        #check for h or s
                        displayText(screen, black, green, "(h)it or (s)tay?", 25, (200, 290))
                        displayText(screen, black, green, "%d"%(player.handValue), 20, (100, 520))
                        pygame.display.update()
                        if twoButton(K_h, K_s):
                            player.hit(d)
                            player.handValue = player.getHandValue() # TODO
                            playerCardIDs = player.cardIDs()
                            displayGUICards(playerCardIDs, screen, 375)
                            displayText(screen, black, green, "%d"%(player.handValue), 20, (100, 520))
                            pygame.display.update()
                            time.sleep(0.5)         
                        else:
                            playerEndGame = False
                            break
                        
                        #determine win or lose
                        if player.handValue > 21:
                            displayText(screen, black, red, "You Busted!", 125, (200, 250))
                            pygame.display.update()
                            playerEndGame = True
                            break
                        elif player.handValue == 21:
                            displayText(screen, black, red, "You Win!", 125, (200, 250))
                            pygame.display.update()
                            playerEndGame = True
                            break
                
                dealerEndGame = False
                if not playerEndGame:
                    while True:
                        dealerCardIDs = dealer.cardIDs()
                        displayGUICards(dealerCardIDs, screen, 125)
                        displayText(screen, black, green, "%d"%(dealer.handValue), 20, (100, 70))
                        pygame.display.update()
                        if dealer.handValue == 21:
                            displayText(screen, black, green, "%d"%(dealer.handValue), 20, (100, 70))
                            displayText(screen, black, red, "Dealer Wins!", 125, (200, 250))
                            dealerEndGame = True
                            pygame.display.update()
                            break
                        elif dealer.handValue > 21:
                            displayText(screen, black, green, "%d"%(dealer.handValue), 20, (100, 70))
                            displayText(screen, black, red, "You Win!", 125, (200, 250))
                            dealerEndGame = True
                            pygame.display.update()
                            break
                        elif dealer.handValue >= 17:
                            break
                        elif dealer.handValue < 17:
                            dealer.hit(d)
                            time.sleep(1)
                            
                    if not dealerEndGame:
                        if player.handValue > dealer.handValue:
                            displayText(screen, black, red, "You Win!", 125, (200, 250))
                            pygame.display.update()
                        elif player.handValue == dealer.handValue:
                            displayText(screen, black, red, "You Push!", 125, (200, 250))
                            pygame.display.update()
                        elif player.handValue < dealer.handValue:
                            displayText(screen, black, red, "Dealer Wins!", 125, (200, 250))
                            pygame.display.update()

                # Play again
                screen.fill(green)
                displayText(screen, black, green, "Pla(y) agai(n)?", 125, (165, 250))
                time.sleep(2)
                pygame.display.update()
                if twoButton(K_y, K_n):
                    break
                else:
                    pygame.quit()
                    sys.exit()
                
        FramePerSec.tick(FPS)

main()
